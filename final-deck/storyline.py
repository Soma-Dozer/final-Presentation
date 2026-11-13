"""2026-11-13: group collaboration slides between Development and Effect.

Select by source and title, so later slide insertions do not change the targets.
Original layouts, evidence, and notes remain owned by their section modules.
"""
import html
import re
from core import divider


TEAMWORK = [
    ('s1_intro', '팀 소개', None,
     '지금까지 소개한 DevFit을 함께 만든 팀의 협업 과정을 말씀드리겠습니다.'),
    ('s1_intro', '학업도 병행했습니다.', None,
     '학업 병행 이야기 뒤에 중간고사 결과를 짧은 에피소드로 소개하고 수행 과정으로 넘어갑니다.'),
    ('s1_intro', '멘토 소개', None,
     '각자의 역할을 나누고, 비즈니스·개발·AI 분야의 멘토진과 방향을 검토했습니다.'),
    ('s3_effect', '피봇 후 MVP 구축,', None,
     '이런 역할 분담으로 피봇 이후 첫 출시까지 함께 진행했습니다.'),
    ('s3_effect', '음성 모의 면접 도입,', None,
     '출시 후에는 피드백을 바탕으로 질문 품질과 기능을 개선하고 서비스 운영 범위를 넓혔습니다.'),
    ('s2_dev', '수행과정', '피드백을 운영에 반영한 <span class="purple">협업 성과</span>',
     '이 과정의 결과를 피드백 대응과 운영 배포 기록으로 정리했습니다.'),
    # 2026-11-13 사용자: 사업자, 직업정보, 특허 3장을 수행과정 성과 장 뒤로 이동
    ('s3_effect', '사업자등록 · 통신판매업', None,
     '개발과 함께 서비스를 운영하고 결제를 받기 위한 사업 절차도 마쳤습니다.'),
    ('s3_effect', '직업정보제공사업 신고', None,
     '채용공고를 모아 보여 주는 서비스라 직업정보제공사업 신고도 했습니다.'),
    ('s3_effect', '핵심 기술 3건', None,
     '그리고 핵심 기술은 특허로 출원했습니다.'),
]


def arrange(main, appendix):
    main, appendix = list(main), list(appendix)
    teamwork = []
    for source, title_prefix, heading, transition in TEAMWORK:
        matches = []
        for collection in (main, appendix):
            for i, (name, markup, note) in enumerate(collection):
                title = html.unescape(re.search(r'data-title="([^"]*)"', markup)[1])
                if name == source and title.startswith(title_prefix):
                    matches.append((collection, i))
        if len(matches) != 1:
            raise ValueError(f'Expected one teamwork slide: {source} / {title_prefix}; found {len(matches)}')
        collection, i = matches[0]
        _, markup, note = collection.pop(i)
        markup = re.sub(r'(<section\b[^>]*class=")([^"]*)',
                        lambda m: m[1] + m[2] + ' teamwork-slide', markup, count=1)
        markup = re.sub(r'(<div class="eyebrow">).*?(</div>)', r'\1Teamwork\2', markup, count=1)
        if heading:
            markup = re.sub(r'(<h1\b[^>]*>).*?(</h1>)', lambda m: m[1]+heading+m[2], markup, count=1, flags=re.S)
            title = html.escape(re.sub(r'<[^>]*>', '', heading), quote=True)
            markup = re.sub(r'data-title="[^"]*"', lambda m: f'data-title="{title}"', markup, count=1)
        markup = '\n'.join(line.rstrip() for line in markup.split('\n'))
        teamwork.append(('teamwork', markup, '[장 연결] '+transition+'\n\n'+note))
    effect = [i for i, (_, markup, _) in enumerate(main) if 'data-title="Effect"' in markup]
    if len(effect) != 1:
        raise ValueError('Expected one Effect divider')
    chapter = divider('04 · 협업', 'Teamwork', '역할 분담, 협업 방식, 수행 과정과 피드백 반영')
    chapter = chapter.replace('class="slide divider"', 'class="slide divider teamwork-divider"', 1)
    chapter_note = '[구분] 앞에서 소개한 기술을 함께 구현한 팀과 협업 과정을 소개합니다. 역할 분담과 멘토진, 학업과 병행한 협업, 출시 전후의 수행 과정, 피드백 반영 성과의 순서로 이어집니다.'
    main[effect[0]:effect[0]] = [('teamwork', chapter, chapter_note), *teamwork]
    return main, appendix
