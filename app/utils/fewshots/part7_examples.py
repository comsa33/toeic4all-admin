class Part7SinglePassageFewShotExamples:
    """
    TOEIC Part 7 single-passage few-shot examples
    ─ 각 지문 유형 1세트, 문항 2–4개, questionType 다양화 ─
    """

    # 1) Email
    email = [
        {
            "part": 7,
            "difficulty": "Easy",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Email",
                    "text": (
                        "Subject: System Downtime Notice\n\n"
                        "Dear Staff,\n\n"
                        "Please be advised that our payroll system will be offline for "
                        "scheduled maintenance from 8 p.m. this Friday until 6 a.m. Saturday. "
                        "During this time, you will not be able to access pay stubs or submit "
                        "time-off requests. We apologize for any inconvenience and appreciate "
                        "your understanding.\n\n"
                        "Regards,\nIT Support"
                    ),
                    "translation": (
                        "제목: 시스템 중단 공지\n\n"
                        "친애하는 직원 여러분,\n\n"
                        "우리 급여 시스템이 이번 금요일 오후 8시부터 토요일 오전 6시까지 예정된 유지 보수로 "
                        "오프라인 상태가 될 것임을 알려드립니다. 이 시간 동안 급여 명세서에 접근하거나 "
                        "휴가 요청을 제출할 수 없습니다. 불편을 드려 죄송하며 이해해 주셔서 감사합니다.\n\n"
                        "감사합니다,\nIT 지원팀"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "Why was this e-mail sent?",
                    "questionTranslation": "이 이메일이 발송된 주된 이유는 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To announce a system upgrade",
                            "translation": "시스템 업그레이드를 알리기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To notify employees of system downtime",
                            "translation": "시스템 중단을 알리기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To request time-off forms",
                            "translation": "휴가 신청서를 요청하기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To distribute pay stubs",
                            "translation": "급여 명세서를 배포하기 위해",
                        },
                    ],
                    "answer": "B",
                    "explanation": "본문 첫 문단에서 점검으로 인한 중단 시간을 직원에게 알린다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "How long will the maintenance last?",
                    "questionTranslation": "점검은 얼마나 지속됩니까?",
                    "choices": [
                        {"id": "A", "text": "6 hours", "translation": "6시간"},
                        {"id": "B", "text": "8 hours", "translation": "8시간"},
                        {"id": "C", "text": "10 hours", "translation": "10시간"},
                        {"id": "D", "text": "12 hours", "translation": "12시간"},
                    ],
                    "answer": "C",
                    "explanation": "금요일 20시부터 토요일 6시까지는 10시간이다.",
                },
            ],
        },
        # difficulty: "Medium" 예시 추가 - 지문이 훨씬 더 길어짐
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Email",
                    "text": (
                        "Subject: Upcoming Team Retreat\n\n"
                        "Dear Team,\n\n"
                        "I am excited to announce that we will be having a team retreat "
                        "next month at the Green Mountain Lodge. The retreat will take "
                        "place from September 15 to September 17. This is a great opportunity "
                        "for us to bond as a team and discuss our goals for the upcoming "
                        "quarter.\n\n"
                        "In addition to team-building activities and strategy sessions, "
                        "we have arranged for several guest speakers to share insights on "
                        "leadership and innovation. There will also be outdoor events such as "
                        "a guided hike and a group cooking challenge. All meals and lodging "
                        "will be provided, and transportation will be arranged from the office "
                        "on the morning of September 15.\n\n"
                        "Please mark your calendars and let me know if you have any dietary "
                        "restrictions or special requests. If you need to adjust your work "
                        "schedule or have concerns about attending, please reach out to me "
                        "directly. A detailed agenda and packing list will be sent out next week.\n\n"
                        "I look forward to seeing all of you there!\n\n"
                        "Best,\n"
                        "Sarah Johnson\n"
                        "Team Leader"
                    ),
                    "translation": (
                        "제목: 다가오는 팀 리트릿\n\n"
                        "친애하는 팀 여러분,\n\n"
                        "다음 달에 그린 마운틴 로지에서 팀 리트릿을 개최하게 되어 기쁩니다. "
                        "리트릿은 9월 15일부터 9월 17일까지 진행됩니다. 이는 우리가 팀으로서 "
                        "유대감을 형성하고 다가오는 분기의 목표에 대해 논의할 수 있는 좋은 기회입니다.\n\n"
                        "팀워크를 위한 다양한 활동과 전략 세션 외에도, 리더십과 혁신에 대한 인사이트를 "
                        "공유해 줄 여러 명의 외부 연사도 초청했습니다. 또한 가이드와 함께하는 하이킹, "
                        "단체 요리 대회 등 야외 이벤트도 준비되어 있습니다. 모든 식사와 숙박이 제공되며, "
                        "9월 15일 아침 사무실에서 출발하는 교통편도 마련될 예정입니다.\n\n"
                        "달력에 표시해 주시고 식이 제한이나 특별 요청 사항이 있으면 알려주세요. "
                        "근무 일정 조정이 필요하거나 참석에 대해 궁금한 점이 있으면 언제든 저에게 "
                        "직접 연락해 주세요. 자세한 일정표와 준비물 목록은 다음 주에 안내드리겠습니다.\n\n"
                        "모두 뵙기를 기대합니다!\n\n"
                        "감사합니다,\n"
                        "Sarah Johnson\n팀장"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "What is the main purpose of this email?",
                    "questionTranslation": "이 이메일의 주된 목적은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To announce a team retreat",
                            "translation": "팀 리트릿을 알리기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To schedule a meeting",
                            "translation": "회의 일정을 잡기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To discuss project updates",
                            "translation": "프로젝트 업데이트를 논의하기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To request feedback on a report",
                            "translation": "보고서에 대한 피드백을 요청하기 위해",
                        },
                    ],
                    "answer": "A",
                    "explanation": "'팀 리트릿 개최'를 알리는 이메일이다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": (
                        "What should team members do if they have dietary restrictions?"
                    ),
                    "questionTranslation": (
                        "팀원들이 식이 제한이 있는 경우 어떻게 해야 합니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "Contact the lodge directly",
                            "translation": "로지에 직접 연락하다",
                        },
                        {
                            "id": "B",
                            "text": "Notify Sarah Johnson",
                            "translation": "Sarah Johnson에게 알리다",
                        },
                        {
                            "id": "C",
                            "text": "Bring their own food",
                            "translation": "자신의 음식을 가져오다",
                        },
                        {
                            "id": "D",
                            "text": "Fill out a form",
                            "translation": "양식을 작성하다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "'식이 제한이나 특별 요청 사항이 있으면 알려주세요'라고 한다.",
                },
            ],
        },
    ]

    # 2) Letter
    letter = [
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Letter",
                    "text": (
                        "789 Oak Avenue\n"
                        "Greenville, TX 75401\n"
                        "April 30, 2025\n\n"
                        "Dear Ms. Rivera,\n\n"
                        "Thank you for meeting with me last week to discuss partnership opportunities between our companies. "
                        "I appreciated your insights regarding the potential for joint product development and market expansion. "
                        "As mentioned during our conversation, I have enclosed a draft contract outlining the proposed terms, "
                        "including the scope of collaboration, project milestones, and payment schedule. Please review the document carefully, "
                        "and let me know if you have any questions or require modifications to any of the clauses.\n\n"
                        "In addition, I would like to highlight that our legal team is available to clarify any legal terminology or compliance requirements. "
                        "If the contract meets your approval, kindly sign and return it by May 15 so that we can initiate the onboarding process and begin the project as planned. "
                        "Should you need more time for internal review, please inform me as soon as possible so we can adjust the timeline accordingly.\n\n"
                        "We are excited about the prospect of working together and believe this partnership will be mutually beneficial. "
                        "Once the agreement is finalized, our project managers will coordinate a kickoff meeting to discuss deliverables, communication protocols, and reporting procedures. "
                        "Thank you again for your time and consideration. I look forward to your response.\n\n"
                        "Sincerely,\n"
                        "Daniel Chan\n"
                        "Business Development Manager"
                    ),
                    "translation": (
                        "789 Oak Avenue\n"
                        "Greenville, TX 75401\n"
                        "2025년 4월 30일\n\n"
                        "친애하는 Rivera 씨,\n\n"
                        "지난주에 저희 회사와의 파트너십 기회에 대해 논의하기 위해 시간을 내주셔서 감사합니다. "
                        "공동 제품 개발 및 시장 확장 가능성에 대한 귀하의 통찰력에 깊이 감사드립니다. "
                        "회의에서 언급한 바와 같이, 제안된 협력 범위, 프로젝트 주요 일정, 그리고 지급 조건이 포함된 계약 초안을 동봉하였습니다. "
                        "문서를 꼼꼼히 검토하시고, 문의 사항이나 조정이 필요한 조항이 있으면 언제든 말씀해 주시기 바랍니다.\n\n"
                        "또한, 저희 법무팀이 법률 용어나 준수 요건에 대해 설명해 드릴 수 있음을 안내드립니다. "
                        "계약서가 귀하의 승인을 받는다면, 5월 15일까지 서명하여 회신해 주시면 온보딩 절차를 시작하고 예정대로 프로젝트를 진행할 수 있습니다. "
                        "내부 검토에 추가 시간이 필요하신 경우, 일정을 조정할 수 있도록 조속히 알려주시기 바랍니다.\n\n"
                        "이번 협력이 상호 이익이 될 것이라 확신하며, 함께 일할 수 있기를 기대합니다. "
                        "계약이 최종 확정되면, 프로젝트 매니저가 착수 회의를 주관하여 산출물, 소통 방식, 보고 절차 등을 논의할 예정입니다. "
                        "다시 한 번 귀한 시간과 관심에 감사드리며, 귀하의 회신을 기다리겠습니다.\n\n"
                        "감사합니다,\n"
                        "Daniel Chan\n"
                        "사업 개발 관리자"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "What does Mr. Chan ask Ms. Rivera to do by May 15?",
                    "questionTranslation": "Chan 씨가 Rivera 씨에게 5월 15일까지 요청한 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Schedule another meeting",
                            "translation": "추가 회의를 일정 잡다",
                        },
                        {
                            "id": "B",
                            "text": "Return a signed contract",
                            "translation": "서명한 계약서를 회신하다",
                        },
                        {
                            "id": "C",
                            "text": "Provide budget figures",
                            "translation": "예산 수치를 제공하다",
                        },
                        {
                            "id": "D",
                            "text": "Send a product sample",
                            "translation": "제품 샘플을 보내다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "본문에서 계약 초안을 서명하여 5월 15일까지 반환해 달라고 요청한다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": "What is implied about the project schedule?",
                    "questionTranslation": "프로젝트 일정에 대해 암시된 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It will start after May 15.",
                            "translation": "5월 15일 이후 시작될 것이다",
                        },
                        {
                            "id": "B",
                            "text": "It has already begun.",
                            "translation": "이미 시작되었다",
                        },
                        {
                            "id": "C",
                            "text": "It depends on another partner.",
                            "translation": "다른 파트너에게 달려 있다",
                        },
                        {
                            "id": "D",
                            "text": "It was cancelled.",
                            "translation": "취소되었다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "계약서 회신을 받아야 온보딩 및 프로젝트를 예정대로 시작할 수 있다고 언급한다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "주제/목적",
                    "questionText": "What is the main purpose of this letter?",
                    "questionTranslation": "이 편지의 주된 목적은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To confirm a meeting date",
                            "translation": "회의 일정을 확정하기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To request contract review and approval",
                            "translation": "계약서 검토 및 승인을 요청하기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To introduce a new product",
                            "translation": "신제품을 소개하기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To discuss payment issues",
                            "translation": "지급 문제를 논의하기 위해",
                        },
                    ],
                    "answer": "B",
                    "explanation": "계약 초안 검토 및 서명을 요청하는 내용이 편지의 핵심이다.",
                },
            ],
        }
    ]

    # 3) Memo
    memo = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Memo",
                    "text": (
                        "MEMORANDUM\n\n"
                        "To: All Research Department Staff\n"
                        "From: Dr. Emily Park, Laboratory Director\n"
                        "Date: June 12, 2025\n"
                        "Subject: Comprehensive Safety Audit—Findings and Required Actions\n\n"
                        "Following last week’s extensive safety audit, several critical issues have been identified that require immediate attention. "
                        "The audit revealed that multiple chemical storage areas lack updated hazard labels, and some emergency exits were partially obstructed by equipment or storage boxes. "
                        "Additionally, it was noted that the eyewash stations in Labs 3 and 5 have not been tested in the past six months, and the spill response kits are missing key supplies such as absorbent pads and gloves.\n\n"
                        "To address these concerns, all team leaders must submit detailed corrective action plans by June 26. "
                        "These plans should include a timeline for relabeling all chemical containers according to the new GHS standards, a schedule for monthly emergency-exit inspections, and a checklist for restocking safety equipment. "
                        "Furthermore, please ensure that all staff complete the updated online safety training module by July 1. "
                        "Failure to comply with these requirements may result in restricted access to laboratory facilities until deficiencies are resolved.\n\n"
                        "If you have questions regarding the audit findings or need assistance developing your action plans, contact the Safety Office at extension 204. "
                        "Thank you for your cooperation in maintaining a safe and compliant research environment."
                    ),
                    "translation": (
                        "메모\n\n"
                        "수신: 연구 부서 전 직원\n"
                        "발신: Dr. Emily Park, 실험실장\n"
                        "날짜: 2025년 6월 12일\n"
                        "제목: 종합 안전 감사—결과 및 필수 조치\n\n"
                        "지난주 실시된 대규모 안전 감사 결과, 즉각적인 조치가 필요한 여러 중대한 문제가 확인되었습니다. "
                        "감사에서는 다수의 화학 물질 저장 구역에 최신 위험 라벨이 부착되어 있지 않으며, 일부 비상 출구가 장비나 보관 상자에 의해 부분적으로 막혀 있는 것으로 드러났습니다. "
                        "또한 3번 및 5번 실험실의 세안기가 최근 6개월간 점검되지 않았고, 유출 대응 키트에는 흡수 패드와 장갑 등 주요 용품이 빠져 있는 것으로 확인되었습니다.\n\n"
                        "이러한 문제를 해결하기 위해 모든 팀 리더는 6월 26일까지 구체적인 시정 조치 계획을 제출해야 합니다. "
                        "계획서에는 새로운 GHS 기준에 따라 모든 화학 용기 라벨을 교체하는 일정, 월별 비상 출구 점검 일정, 안전 장비 재고 점검 체크리스트가 포함되어야 합니다. "
                        "아울러, 전 직원은 7월 1일까지 업데이트된 온라인 안전 교육을 반드시 이수해야 합니다. "
                        "이 요구 사항을 준수하지 않을 경우, 미비 사항이 해결될 때까지 실험실 출입이 제한될 수 있습니다.\n\n"
                        "감사 결과나 시정 계획 수립에 관한 문의는 내선 204번 안전관리실로 연락해 주시기 바랍니다. "
                        "안전하고 준법적인 연구 환경 유지를 위한 협조에 감사드립니다."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "What is the main purpose of this memo?",
                    "questionTranslation": "이 메모의 주된 목적은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To announce new research projects",
                            "translation": "새 연구 프로젝트를 알리기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To report audit results and outline required safety actions",
                            "translation": "감사 결과를 보고하고 필수 안전 조치를 안내하기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To schedule laboratory renovations",
                            "translation": "실험실 리노베이션 일정을 잡기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To request budget proposals",
                            "translation": "예산안을 요청하기 위해",
                        },
                    ],
                    "answer": "B",
                    "explanation": "감사 결과와 시정 조치 계획 제출, 교육 이수 등 구체적 안전 조치 안내가 핵심이다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "According to the memo, which of the following is NOT mentioned as a safety issue?",
                    "questionTranslation": "메모에 따르면 다음 중 안전 문제로 언급되지 않은 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Obstructed emergency exits",
                            "translation": "막힌 비상 출구",
                        },
                        {
                            "id": "B",
                            "text": "Expired chemical labels",
                            "translation": "만료된 화학 라벨",
                        },
                        {
                            "id": "C",
                            "text": "Uninspected eyewash stations",
                            "translation": "점검되지 않은 세안기",
                        },
                        {
                            "id": "D",
                            "text": "Missing spill response supplies",
                            "translation": "유출 대응 용품 부족",
                        },
                    ],
                    "answer": "B",
                    "explanation": "라벨 미갱신(업데이트 안 됨)은 언급되나 '만료'라는 표현은 없다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "추론",
                    "questionText": "What can be inferred about laboratory access after July 1?",
                    "questionTranslation": "7월 1일 이후 실험실 출입에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Only team leaders will have access.",
                            "translation": "팀 리더만 출입할 수 있다",
                        },
                        {
                            "id": "B",
                            "text": "Access may be restricted for non-compliance.",
                            "translation": "미이행 시 출입이 제한될 수 있다",
                        },
                        {
                            "id": "C",
                            "text": "All staff will be required to work remotely.",
                            "translation": "전 직원이 재택근무해야 한다",
                        },
                        {
                            "id": "D",
                            "text": "Access will be granted without conditions.",
                            "translation": "조건 없이 출입이 허용된다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "요구 사항 미이행 시 출입 제한 가능성이 명시되어 있다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "어휘",
                    "questionText": "In the memo, the word “deficiencies” is closest in meaning to ____.",
                    "questionTranslation": "메모에서 'deficiencies'는 문맥상 어떤 의미와 가장 가깝습니까?",
                    "choices": [
                        {"id": "A", "text": "improvements", "translation": "개선점"},
                        {
                            "id": "B",
                            "text": "shortcomings",
                            "translation": "결함/미비점",
                        },
                        {"id": "C", "text": "instructions", "translation": "지침"},
                        {"id": "D", "text": "procedures", "translation": "절차"},
                    ],
                    "answer": "B",
                    "explanation": "'deficiencies'는 부족함, 결함, 미비점을 의미한다.",
                },
            ],
        }
    ]

    # 4) Notice
    notice = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Notice",
                    "text": (
                        "**Notice of Scheduled Water Shutdown and Facility Access Restrictions**\n\n"
                        "To: All Tenants and Building Staff\n"
                        "From: Building Management Office\n"
                        "Date: June 25, 2025\n"
                        "Subject: Water Supply Interruption and Temporary Facility Closures—July 8\n\n"
                        "Please be advised that the building’s water supply will be completely shut off on Tuesday, July 8, from 10:00 a.m. to 2:00 p.m. to allow for essential pipe replacement and maintenance work on all floors. During this four-hour period, all restroom facilities, kitchen sinks, and water fountains will be unavailable. In addition, the laundry room and shower areas on the basement level will be closed for the duration of the shutdown.\n\n"
                        "Tenants are strongly encouraged to make necessary arrangements in advance. If you require water for cleaning, cooking, or other purposes, please store an adequate supply before the scheduled shutdown. Bottled water will be available for purchase at the lobby convenience store, but supplies may be limited. Please note that the building’s fire suppression system will remain operational throughout the maintenance.\n\n"
                        "Contractors will be working in the main utility corridors and may require temporary access to individual units to inspect water lines. If your presence is needed, you will be notified by phone or email at least 24 hours in advance. We ask for your cooperation in granting access to ensure the work is completed safely and efficiently.\n\n"
                        "We apologize for any inconvenience this may cause and appreciate your understanding as we work to improve building infrastructure. For questions or urgent concerns, contact the management office at extension 301 or email support@buildingoffice.com.\n\n"
                        "Thank you for your cooperation."
                    ),
                    "translation": (
                        "**예정된 단수 및 시설 이용 제한 안내**\n\n"
                        "수신: 전 입주자 및 건물 직원\n"
                        "발신: 건물 관리사무소\n"
                        "날짜: 2025년 6월 25일\n"
                        "제목: 7월 8일 수도 공급 중단 및 임시 시설 폐쇄 안내\n\n"
                        "전 층 배관 교체 및 유지보수 작업으로 인해 7월 8일(화) 오전 10시부터 오후 2시까지 건물 전체의 수도 공급이 완전히 중단됩니다. 이 4시간 동안 모든 화장실, 주방 싱크대, 정수기 사용이 불가합니다. 또한 지하층 세탁실과 샤워실도 단수 시간 동안 폐쇄됩니다.\n\n"
                        "청소, 요리 등 용수 사용이 필요한 경우 사전에 충분한 물을 비축해 주시기 바랍니다. 로비 편의점에서 생수를 구매할 수 있으나, 수량이 제한될 수 있습니다. 단, 건물의 화재 진압 시스템(스프링클러 등)은 정상 작동합니다.\n\n"
                        "작업 당일 주요 설비 구역에서 외부 인력이 작업할 예정이며, 필요 시 각 세대의 수도관 점검을 위해 일시적으로 출입을 요청드릴 수 있습니다. 입주자 협조가 필요한 경우 최소 24시간 전에 전화 또는 이메일로 개별 안내드릴 예정이오니, 안전하고 신속한 작업을 위해 출입에 협조 부탁드립니다.\n\n"
                        "불편을 드려 죄송하며, 건물 시설 개선을 위한 조치이오니 양해 부탁드립니다. 문의 사항이나 긴급 요청은 내선 301번 또는 support@buildingoffice.com으로 연락해 주시기 바랍니다.\n\n"
                        "협조에 감사드립니다."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "Which of the following facilities will NOT be available during the water shutdown?",
                    "questionTranslation": "단수 시간 동안 이용할 수 없는 시설이 아닌 것은 무엇입니까?",
                    "choices": [
                        {"id": "A", "text": "Restrooms", "translation": "화장실"},
                        {
                            "id": "B",
                            "text": "Kitchen sinks",
                            "translation": "주방 싱크대",
                        },
                        {
                            "id": "C",
                            "text": "Fire suppression system",
                            "translation": "화재 진압 시스템",
                        },
                        {"id": "D", "text": "Laundry room", "translation": "세탁실"},
                    ],
                    "answer": "C",
                    "explanation": "화재 진압 시스템(스프링클러 등)은 정상 작동한다고 안내되어 있다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": "What can be inferred about the availability of bottled water during the shutdown?",
                    "questionTranslation": "단수 기간 동안 생수 공급에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It will be provided free of charge to all tenants.",
                            "translation": "모든 입주자에게 무료로 제공된다",
                        },
                        {
                            "id": "B",
                            "text": "It can be purchased at the lobby store, but may run out.",
                            "translation": "로비 편의점에서 구매할 수 있으나 품절될 수 있다",
                        },
                        {
                            "id": "C",
                            "text": "It will be delivered to each unit by management.",
                            "translation": "관리사무소에서 각 세대로 배달된다",
                        },
                        {
                            "id": "D",
                            "text": "It is not available anywhere in the building.",
                            "translation": "건물 내 어디에서도 구할 수 없다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "로비 편의점에서 구매 가능하나 수량이 제한될 수 있다고 명시되어 있다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "세부사항",
                    "questionText": "How will tenants be notified if contractors need to access their units?",
                    "questionTranslation": "외부 인력이 세대 출입이 필요한 경우 입주자에게 어떻게 안내됩니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A notice will be posted on the main entrance.",
                            "translation": "정문에 공지가 부착된다",
                        },
                        {
                            "id": "B",
                            "text": "They will be contacted at least 24 hours in advance.",
                            "translation": "최소 24시간 전에 개별 연락을 받는다",
                        },
                        {
                            "id": "C",
                            "text": "A message will be sent via text only.",
                            "translation": "문자 메시지만 발송된다",
                        },
                        {
                            "id": "D",
                            "text": "No prior notice will be given.",
                            "translation": "사전 안내가 없다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "전화 또는 이메일로 최소 24시간 전에 안내한다고 명시되어 있다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "주제/목적",
                    "questionText": "What is the main purpose of this notice?",
                    "questionTranslation": "이 공지문의 주된 목적은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To inform tenants of a scheduled water shutdown and related facility closures",
                            "translation": "예정된 단수 및 관련 시설 폐쇄를 알리기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To announce a fire drill",
                            "translation": "소방 훈련을 알리기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To request payment of maintenance fees",
                            "translation": "관리비 납부를 요청하기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To introduce new building staff",
                            "translation": "신규 직원 소개를 위해",
                        },
                    ],
                    "answer": "A",
                    "explanation": "단수 일정, 시설 이용 제한, 협조 요청 등 단수 관련 안내가 주 목적이다.",
                },
            ],
        }
    ]

    # 5) Advertisement
    advertisement = [
        {
            "part": 7,
            "difficulty": "Easy",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Advertisement",
                    "text": (
                        "**Summer Fitness Pass—Limited Offer!**\n\n"
                        "Ready to get in shape this summer? Riverside Gym is excited to announce our exclusive Summer Fitness Pass promotion! "
                        "Sign up before June 30 and enjoy three full months of unlimited access to all gym facilities—including our state-of-the-art cardio zone, "
                        "free weights, group fitness classes (yoga, pilates, HIIT, and more), and the indoor swimming pool—for only $99. "
                        "This offer is available to new and returning members who have not held a membership in the past six months.\n\n"
                        "As an added bonus, the first 100 sign-ups will receive a complimentary personal-training session with one of our certified trainers. "
                        "During your session, you’ll receive a customized workout plan and a body composition analysis to help you reach your fitness goals faster. "
                        "All Summer Fitness Pass holders will also receive a 10% discount on nutrition counseling and merchandise at our pro shop.\n\n"
                        "Riverside Gym is open from 5 a.m. to 11 p.m. on weekdays and 7 a.m. to 9 p.m. on weekends. "
                        "Locker rooms, towel service, and free parking are included. To enroll, visit our front desk or sign up online at www.riversidegym.com/summerpass. "
                        "For questions, call (555) 123-4567 or email info@riversidegym.com.\n\n"
                        "Don’t miss this chance to make the most of your summer—spaces are limited and this offer will not be extended!"
                    ),
                    "translation": (
                        "**여름 피트니스 패스—한정 제공!**\n\n"
                        "올여름 건강한 변화를 원하시나요? 리버사이드 체육관에서 여름 한정 피트니스 패스 프로모션을 진행합니다! "
                        "6월 30일 이전에 등록하시면 최신식 유산소 존, 프리웨이트, 다양한 그룹 운동 수업(요가, 필라테스, HIIT 등), 실내 수영장 등 "
                        "모든 시설을 3개월간 무제한으로 이용하실 수 있습니다. 가격은 단 $99이며, 최근 6개월 이내 회원이 아니었던 신규 및 재가입 고객 모두 신청 가능합니다.\n\n"
                        "또한, 선착순 100명에게는 공인 트레이너와의 무료 개인 트레이닝 세션이 제공됩니다. "
                        "이 세션에서는 맞춤형 운동 계획과 체성분 분석을 통해 목표 달성을 도와드립니다. "
                        "모든 여름 패스 회원에게는 영양 상담 및 프로샵 상품 10% 할인 혜택도 드립니다.\n\n"
                        "리버사이드 체육관은 평일 오전 5시~오후 11시, 주말 오전 7시~오후 9시까지 운영됩니다. "
                        "락커룸, 타월 서비스, 무료 주차가 모두 포함되어 있습니다. 등록은 프런트 데스크 방문 또는 www.riversidegym.com/summerpass에서 온라인 신청이 가능합니다. "
                        "문의: (555) 123-4567 또는 info@riversidegym.com으로 연락 주세요.\n\n"
                        "이번 여름을 놓치지 마세요—좌석이 한정되어 있으며, 본 프로모션은 연장되지 않습니다!"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "What is the advertisement promoting?",
                    "questionTranslation": "이 광고는 무엇을 홍보하고 있습니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A fitness pass discount",
                            "translation": "피트니스 패스 할인",
                        },
                        {
                            "id": "B",
                            "text": "New gym equipment",
                            "translation": "새 운동 기구",
                        },
                        {
                            "id": "C",
                            "text": "A nutrition seminar",
                            "translation": "영양 세미나",
                        },
                        {
                            "id": "D",
                            "text": "Gym renovations",
                            "translation": "헬스장 리노베이션",
                        },
                    ],
                    "answer": "A",
                    "explanation": "여름 한정 피트니스 패스를 할인된 가격에 홍보한다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "Which of the following is NOT included with the Summer Fitness Pass?",
                    "questionTranslation": "여름 피트니스 패스에 포함되지 않은 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Unlimited access to group classes",
                            "translation": "그룹 수업 무제한 이용",
                        },
                        {"id": "B", "text": "Free parking", "translation": "무료 주차"},
                        {
                            "id": "C",
                            "text": "A guaranteed free personal-training session for all",
                            "translation": "모든 회원 대상 무료 PT 세션 보장",
                        },
                        {
                            "id": "D",
                            "text": "Locker room use",
                            "translation": "락커룸 이용",
                        },
                    ],
                    "answer": "C",
                    "explanation": "무료 PT 세션은 선착순 100명에게만 제공된다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "추론",
                    "questionText": "What can be inferred about the gym’s operating hours?",
                    "questionTranslation": "체육관 운영 시간에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It opens earlier on weekends.",
                            "translation": "주말에 더 일찍 연다",
                        },
                        {
                            "id": "B",
                            "text": "It closes later on weekdays.",
                            "translation": "평일에 더 늦게 닫는다",
                        },
                        {
                            "id": "C",
                            "text": "It is open 24 hours.",
                            "translation": "24시간 운영한다",
                        },
                        {
                            "id": "D",
                            "text": "It is closed on Sundays.",
                            "translation": "일요일은 휴관이다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "평일(오전 5시~오후 11시)이 주말(오전 7시~오후 9시)보다 더 늦게까지 운영한다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "세부사항",
                    "questionText": "Who is eligible for the Summer Fitness Pass promotion?",
                    "questionTranslation": "여름 피트니스 패스 프로모션 신청 자격이 있는 사람은 누구입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Only current members",
                            "translation": "현재 회원만",
                        },
                        {
                            "id": "B",
                            "text": "Anyone who has not been a member in the past 6 months",
                            "translation": "최근 6개월 이내 회원이 아니었던 사람",
                        },
                        {"id": "C", "text": "Only students", "translation": "학생만"},
                        {
                            "id": "D",
                            "text": "Only first-time visitors",
                            "translation": "첫 방문자만",
                        },
                    ],
                    "answer": "B",
                    "explanation": "최근 6개월 이내 회원이 아니었던 신규 및 재가입 고객이 대상이다.",
                },
            ],
        }
    ]

    # 6) Article
    article = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Article",
                    "text": (
                        "Local Startup Wins Innovation Award\n\n"
                        "GreenWave Technologies, a company specializing in ocean-cleaning robots, received this year’s Global Innovation Award on Monday. "
                        "The firm’s automated vessels can collect up to five tons of plastic debris daily, helping coastal cities keep waterways clear.\n\n"
                        "Founded in 2018 by marine engineer Lisa Kim, GreenWave Technologies began as a small research project at a local university. "
                        "The company’s mission is to develop sustainable solutions for marine pollution, which has become a growing concern for coastal communities worldwide. "
                        "According to the International Oceanic Foundation, over eight million tons of plastic waste enter the oceans each year, threatening marine life and human health.\n\n"
                        "GreenWave’s flagship product, the AquaSweep 3000, uses advanced sensors and artificial intelligence to identify and collect floating debris. "
                        "The vessel operates autonomously, navigating busy harbors and rivers while avoiding boats and wildlife. "
                        "Collected waste is sorted onboard, with recyclable materials separated from general trash. "
                        "The company has partnered with local recycling centers to ensure that as much collected plastic as possible is reused.\n\n"
                        "The award ceremony, held at the Global Technology Forum in Singapore, recognized GreenWave’s significant contribution to environmental protection. "
                        "In her acceptance speech, CEO Lisa Kim emphasized the importance of collaboration: “Solving the plastic crisis requires teamwork between technology developers, governments, and the public. "
                        "We are proud to work with city officials and volunteers to keep our oceans clean.”\n\n"
                        "GreenWave’s technology has already been adopted by several coastal cities in Asia and Europe. "
                        "In Busan, South Korea, the city government reported a 30% reduction in visible plastic waste along the shoreline after deploying two AquaSweep vessels last year. "
                        "Similar results were observed in Rotterdam, where the robots helped clear canals used for both tourism and shipping.\n\n"
                        "Looking ahead, GreenWave plans to expand its fleet and develop new models capable of operating in rougher seas. "
                        "The company is also working on educational programs to raise awareness about plastic pollution and encourage responsible waste disposal. "
                        "“Technology alone can’t solve the problem,” Kim noted. “We need everyone to take part in protecting our oceans for future generations.”"
                    ),
                    "translation": (
                        "지역 스타트업, 혁신상 수상\n\n"
                        "해양 청소 로봇을 전문으로 하는 GreenWave Technologies가 월요일에 올해의 글로벌 혁신상을 수상했습니다. "
                        "이 회사의 자동화된 선박은 매일 최대 5톤의 플라스틱 쓰레기를 수거하여 해안 도시들이 수로를 깨끗하게 유지하는 데 도움을 줍니다.\n\n"
                        "2018년 해양 엔지니어 Lisa Kim이 설립한 GreenWave Technologies는 지역 대학의 소규모 연구 프로젝트로 시작되었습니다. "
                        "이 회사의 사명은 전 세계 해안 지역 사회의 주요 문제로 떠오른 해양 오염에 대한 지속 가능한 해결책을 개발하는 것입니다. "
                        "국제해양재단에 따르면 매년 800만 톤 이상의 플라스틱 폐기물이 바다로 유입되어 해양 생태계와 인류 건강을 위협하고 있습니다.\n\n"
                        "GreenWave의 대표 제품인 AquaSweep 3000은 첨단 센서와 인공지능을 활용해 떠다니는 쓰레기를 식별하고 수거합니다. "
                        "이 선박은 자율적으로 운항하며, 혼잡한 항구와 강에서도 선박 및 야생동물을 피해 안전하게 이동합니다. "
                        "수거된 쓰레기는 선상에서 분류되어 재활용 가능한 플라스틱과 일반 폐기물로 나뉩니다. "
                        "회사는 지역 재활용 센터와 협력해 최대한 많은 플라스틱이 재사용될 수 있도록 하고 있습니다.\n\n"
                        "싱가포르에서 열린 글로벌 테크놀로지 포럼 시상식에서 GreenWave는 환경 보호에 기여한 공로를 인정받았습니다. "
                        "수상 소감에서 CEO Lisa Kim은 협력의 중요성을 강조했습니다. “플라스틱 문제 해결은 기술 개발자, 정부, 시민 모두의 협력이 필요합니다. "
                        "우리는 도시 관계자, 자원봉사자들과 함께 바다를 깨끗하게 지키는 데 자부심을 느낍니다.”\n\n"
                        "GreenWave의 기술은 이미 아시아와 유럽의 여러 해안 도시에서 도입되었습니다. "
                        "한국 부산시에서는 지난해 AquaSweep 선박 2대를 도입한 결과, 해안가의 플라스틱 쓰레기가 30% 감소했다고 보고했습니다. "
                        "관광과 운송에 모두 활용되는 네덜란드 로테르담 운하에서도 유사한 효과가 나타났습니다.\n\n"
                        "앞으로 GreenWave는 선박을 추가 도입하고, 거친 해역에서도 운항 가능한 신모델을 개발할 계획입니다. "
                        "또한 플라스틱 오염의 심각성을 알리고 올바른 폐기 습관을 장려하는 교육 프로그램도 준비 중입니다. "
                        "“기술만으로는 문제를 해결할 수 없습니다. 미래 세대를 위해 모두가 해양 보호에 동참해야 합니다.”라고 Kim 대표는 강조했습니다."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "어휘",
                    "questionText": "In the article, the word 'debris' is closest in meaning to ____.",
                    "questionTranslation": "기사에서 'debris'는 문맥상 어떤 의미와 가장 가깝습니까?",
                    "choices": [
                        {"id": "A", "text": "equipment", "translation": "장비"},
                        {"id": "B", "text": "waste", "translation": "폐기물"},
                        {"id": "C", "text": "fuel", "translation": "연료"},
                        {"id": "D", "text": "cargo", "translation": "화물"},
                    ],
                    "answer": "B",
                    "explanation": "'debris'는 쓰레기·잔해를 뜻한다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": "What can be inferred about GreenWave’s robots?",
                    "questionTranslation": "GreenWave의 로봇에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "They are manually operated.",
                            "translation": "수동으로 조작된다",
                        },
                        {
                            "id": "B",
                            "text": "They help reduce marine pollution.",
                            "translation": "해양 오염을 줄인다",
                        },
                        {
                            "id": "C",
                            "text": "They are still in prototype stage.",
                            "translation": "아직 시제품 단계이다",
                        },
                        {
                            "id": "D",
                            "text": "They require fossil fuel.",
                            "translation": "화석 연료가 필요하다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "하루에 플라스틱 5톤을 수거한다는 내용으로 해양 오염 저감 효과를 알 수 있다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "참조",
                    "questionText": "What does the word 'this year’s' in paragraph 1 refer to?",
                    "questionTranslation": "'this year’s'는 어떤 대상을 가리킵니까?",
                    "choices": [
                        {"id": "A", "text": "The award", "translation": "그 상"},
                        {"id": "B", "text": "The company", "translation": "그 회사"},
                        {"id": "C", "text": "The robots", "translation": "그 로봇들"},
                        {"id": "D", "text": "The cities", "translation": "그 도시들"},
                    ],
                    "answer": "A",
                    "explanation": "'this year’s Global Innovation Award'에서 상을 지칭한다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "세부사항",
                    "questionText": "According to the article, what is one feature of the AquaSweep 3000?",
                    "questionTranslation": "기사에 따르면 AquaSweep 3000의 특징 중 하나는 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It is operated by remote control.",
                            "translation": "원격 조종으로 운항된다",
                        },
                        {
                            "id": "B",
                            "text": "It sorts collected waste onboard.",
                            "translation": "수거한 쓰레기를 선상에서 분류한다",
                        },
                        {
                            "id": "C",
                            "text": "It is only used in Singapore.",
                            "translation": "싱가포르에서만 사용된다",
                        },
                        {
                            "id": "D",
                            "text": "It is powered by solar energy only.",
                            "translation": "태양광만으로 작동한다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "본문에 onboard sorting(선상 분류) 기능이 언급된다.",
                },
            ],
        }
    ]

    # 7) Form
    form = [
        {
            "part": 7,
            "difficulty": "Easy",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Form",
                    "text": (
                        "International Business Conference 2025 — Registration Form (Excerpt)\n\n"
                        "Full Name: _______________________________\n"
                        "Company/Organization: _____________________\n"
                        "Job Title: ________________________________\n"
                        "Email Address: ____________________________\n"
                        "Phone Number: _____________________________\n"
                        "Country of Residence: _____________________ (A)\n"
                        "\n"
                        "Conference Sessions (Select up to 2):\n"
                        "  □ A. Global Market Trends\n"
                        "  □ B. Digital Transformation\n"
                        "  □ C. Leadership & Management\n"
                        "  □ D. Sustainable Business\n"
                        "\n"
                        "Workshop Participation (Choose one):\n"
                        "  □ Morning (9:00–12:00)   □ Afternoon (14:00–17:00) (B)\n"
                        "\n"
                        "Dietary Requirements (Check all that apply):\n"
                        "  □ Vegetarian   □ Vegan   □ Gluten-Free   □ No Preference\n"
                        "\n"
                        "Special Assistance Needed? (Please specify): __________________________\n"
                        "\n"
                        "Payment Method:\n"
                        "  □ Credit Card   □ Bank Transfer   □ On-site Payment (C)\n"
                        "\n"
                        "Signature: ____________________   Date: _______________ (D)\n"
                        "\n"
                        "Note: Early registrants will receive a welcome kit and priority seating for keynote sessions."
                    ),
                    "translation": (
                        "국제 비즈니스 컨퍼런스 2025 — 등록 양식 (일부 발췌)\n\n"
                        "성명: _______________________________\n"
                        "소속/회사: __________________________\n"
                        "직책: _______________________________\n"
                        "이메일 주소: _________________________\n"
                        "전화번호: ____________________________\n"
                        "거주 국가: __________________________ (A)\n"
                        "\n"
                        "컨퍼런스 세션 (최대 2개 선택):\n"
                        "  □ A. 글로벌 시장 동향\n"
                        "  □ B. 디지털 전환\n"
                        "  □ C. 리더십 및 경영\n"
                        "  □ D. 지속가능 경영\n"
                        "\n"
                        "워크숍 참여 (하나 선택):\n"
                        "  □ 오전 (9:00–12:00)   □ 오후 (14:00–17:00) (B)\n"
                        "\n"
                        "식이 요구사항 (해당 사항 모두 체크):\n"
                        "  □ 채식   □ 비건   □ 글루텐 프리   □ 무관\n"
                        "\n"
                        "특별 지원 필요 여부 (구체적으로 기재): __________________________\n"
                        "\n"
                        "결제 방법:\n"
                        "  □ 신용카드   □ 계좌이체   □ 현장 결제 (C)\n"
                        "\n"
                        "서명: ____________________   날짜: _______________ (D)\n"
                        "\n"
                        "참고: 선착순 등록자에게는 웰컴 키트와 기조연설 우선 좌석이 제공됩니다."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "Which of the following is NOT required to complete the registration form?",
                    "questionTranslation": "등록 양식 작성 시 필수 항목이 아닌 것은 무엇입니까?",
                    "choices": [
                        {"id": "A", "text": "Job Title", "translation": "직책"},
                        {
                            "id": "B",
                            "text": "Special Assistance Needed",
                            "translation": "특별 지원 필요 여부",
                        },
                        {
                            "id": "C",
                            "text": "Email Address",
                            "translation": "이메일 주소",
                        },
                        {"id": "D", "text": "Signature", "translation": "서명"},
                    ],
                    "answer": "B",
                    "explanation": "특별 지원 필요 여부는 해당자만 작성하는 선택 항목이다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "문장삽입",
                    "questionText": "Where would the following sentence best fit?\n"
                    '"Please indicate your preferred language for conference materials."\n',
                    "questionTranslation": "다음 문장을 어디에 삽입하는 것이 가장 적절합니까?\n"
                    '"컨퍼런스 자료의 선호 언어를 표시해 주십시오."',
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "A",
                    "explanation": "참가자 정보(국가)와 함께 언어 선호를 묻는 것이 자연스럽다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "추론",
                    "questionText": "What can be inferred about the conference workshops?",
                    "questionTranslation": "컨퍼런스 워크숍에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Participants may attend both morning and afternoon sessions.",
                            "translation": "오전과 오후 모두 참석할 수 있다",
                        },
                        {
                            "id": "B",
                            "text": "Participants must choose only one workshop time slot.",
                            "translation": "하나의 시간대만 선택해야 한다",
                        },
                        {
                            "id": "C",
                            "text": "Workshops are only available to company executives.",
                            "translation": "임원만 워크숍에 참석할 수 있다",
                        },
                        {
                            "id": "D",
                            "text": "Workshops require an additional fee.",
                            "translation": "추가 비용이 필요하다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "오전/오후 중 하나만 선택하도록 되어 있다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "세부사항",
                    "questionText": "What benefit is offered to early registrants?",
                    "questionTranslation": "선착순 등록자에게 제공되는 혜택은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Discounted registration fee",
                            "translation": "등록비 할인",
                        },
                        {
                            "id": "B",
                            "text": "Welcome kit and priority seating",
                            "translation": "웰컴 키트 및 우선 좌석",
                        },
                        {
                            "id": "C",
                            "text": "Free workshop participation",
                            "translation": "무료 워크숍 참여",
                        },
                        {
                            "id": "D",
                            "text": "Complimentary hotel stay",
                            "translation": "무료 호텔 숙박",
                        },
                    ],
                    "answer": "B",
                    "explanation": "본문 하단에 웰컴 키트와 기조연설 우선 좌석 제공이 명시되어 있다.",
                },
            ],
        }
    ]

    # 8) Schedule
    schedule = [
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Schedule",
                    "text": (
                        "Airport Shuttle Bus Timetable (Weekdays)\n\n"
                        "The CityLink shuttle bus operates between Downtown Central Station and International Airport Terminal 1 on weekdays. "
                        "All buses are equipped with free Wi-Fi and luggage racks. Passengers are advised to arrive at the stop at least 10 minutes before departure. "
                        "Tickets can be purchased online or at the station kiosk. For real-time updates, visit www.citylinkbus.com.\n\n"
                        "Downtown → Airport:\n"
                        "06:00   Express (no stops) – Estimated travel time: 40 min\n"
                        "07:30   Regular (stops at Midtown, Riverpark) – Estimated travel time: 55 min\n"
                        "09:00   Regular (stops at Midtown, Riverpark) – Estimated travel time: 55 min\n"
                        "11:00   Express (no stops) – Estimated travel time: 40 min\n"
                        "\n"
                        "Airport → Downtown:\n"
                        "15:00   Regular (stops at Riverpark, Midtown) – Estimated travel time: 55 min\n"
                        "17:00   Express (no stops) – Estimated travel time: 40 min\n"
                        "19:00   Regular (stops at Riverpark, Midtown) – Estimated travel time: 55 min\n"
                        "\n"
                        "Notes:\n"
                        "- The 06:00 and 17:00 buses are express services with no intermediate stops.\n"
                        "- The 07:30, 09:00, 15:00, and 19:00 buses stop at Midtown and Riverpark.\n"
                        "- All buses depart from Platform 3 at their respective locations.\n"
                        "- For questions about accessibility or group bookings, call (555) 234-5678."
                    ),
                    "translation": (
                        "공항 셔틀버스 시간표 (주중)\n\n"
                        "CityLink 셔틀버스는 평일에 다운타운 중앙역과 국제공항 1터미널을 오갑니다. "
                        "모든 버스에는 무료 와이파이와 수하물 선반이 구비되어 있습니다. 승객은 출발 10분 전까지 정류장에 도착해 주시기 바랍니다. "
                        "티켓은 온라인 또는 역 매표기에서 구매할 수 있습니다. 실시간 정보는 www.citylinkbus.com에서 확인하세요.\n\n"
                        "다운타운 → 공항:\n"
                        "06:00   급행 (무정차) – 소요 시간 약 40분\n"
                        "07:30   일반 (미드타운, 리버파크 경유) – 소요 시간 약 55분\n"
                        "09:00   일반 (미드타운, 리버파크 경유) – 소요 시간 약 55분\n"
                        "11:00   급행 (무정차) – 소요 시간 약 40분\n"
                        "\n"
                        "공항 → 다운타운:\n"
                        "15:00   일반 (리버파크, 미드타운 경유) – 소요 시간 약 55분\n"
                        "17:00   급행 (무정차) – 소요 시간 약 40분\n"
                        "19:00   일반 (리버파크, 미드타운 경유) – 소요 시간 약 55분\n"
                        "\n"
                        "비고:\n"
                        "- 06:00, 17:00 버스는 무정차 급행입니다.\n"
                        "- 07:30, 09:00, 15:00, 19:00 버스는 미드타운과 리버파크에 정차합니다.\n"
                        "- 모든 버스는 각 출발지의 3번 승강장에서 출발합니다.\n"
                        "- 교통약자 지원이나 단체 예약 문의는 (555) 234-5678로 연락하세요."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": (
                        "According to the schedule, which morning bus from Downtown to the Airport is the fastest, and what is its estimated travel time?"
                    ),
                    "questionTranslation": (
                        "시간표에 따르면 다운타운에서 공항으로 가는 아침 버스 중 가장 빠른 것은 몇 시 출발이며, 예상 소요 시간은 얼마입니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "06:00, 40 minutes",
                            "translation": "06:00, 40분",
                        },
                        {
                            "id": "B",
                            "text": "07:30, 55 minutes",
                            "translation": "07:30, 55분",
                        },
                        {
                            "id": "C",
                            "text": "09:00, 55 minutes",
                            "translation": "09:00, 55분",
                        },
                        {
                            "id": "D",
                            "text": "11:00, 55 minutes",
                            "translation": "11:00, 55분",
                        },
                    ],
                    "answer": "A",
                    "explanation": "06:00 급행 버스가 무정차로 40분 소요, 가장 빠름.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": (
                        "If a passenger wants to stop at Midtown on the way to the Airport, which departure times should they choose?"
                    ),
                    "questionTranslation": (
                        "공항 가는 길에 미드타운에 정차하려면 몇 시 버스를 이용해야 합니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "07:30 or 09:00",
                            "translation": "07:30 또는 09:00",
                        },
                        {
                            "id": "B",
                            "text": "06:00 or 11:00",
                            "translation": "06:00 또는 11:00",
                        },
                        {
                            "id": "C",
                            "text": "15:00 or 19:00",
                            "translation": "15:00 또는 19:00",
                        },
                        {"id": "D", "text": "17:00 only", "translation": "17:00만"},
                    ],
                    "answer": "A",
                    "explanation": "07:30, 09:00 버스만 미드타운에 정차함.",
                },
            ],
        }
    ]

    # 9) Receipt
    receipt = [
        {
            "part": 7,
            "difficulty": "Easy",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Receipt",
                    "text": (
                        "CITY BOOKSTORE RECEIPT\n\n"
                        "Item            Qty   Price\n"
                        "Notebook         2    $6.00\n"
                        "Pen Set          1    $8.50\n"
                        "Subtotal              $20.50\n"
                        "Tax (5%)               $1.03\n"
                        "Total                  $21.53"
                    ),
                    "translation": (
                        "CITY BOOKSTORE 영수증\n\n"
                        "품목            수량   가격\n"
                        "노트북         2    $6.00\n"
                        "펜 세트          1    $8.50\n"
                        "소계              $20.50\n"
                        "세금 (5%)               $1.03\n"
                        "총계                  $21.53"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "What was the cost of one notebook?",
                    "questionTranslation": "노트 한 권의 가격은 얼마였습니까?",
                    "choices": [
                        {"id": "A", "text": "$3.00", "translation": "$3.00"},
                        {"id": "B", "text": "$6.00", "translation": "$6.00"},
                        {"id": "C", "text": "$8.50", "translation": "$8.50"},
                        {"id": "D", "text": "$12.00", "translation": "$12.00"},
                    ],
                    "answer": "A",
                    "explanation": "노트 2권에 $6이므로 한 권은 $3이다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "참조",
                    "questionText": "In the receipt, what does 'Subtotal' refer to?",
                    "questionTranslation": "영수증에서 'Subtotal'은 무엇을 가리킵니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Total after tax",
                            "translation": "세금 포함 합계",
                        },
                        {
                            "id": "B",
                            "text": "Total before tax",
                            "translation": "세금 제외 합계",
                        },
                        {
                            "id": "C",
                            "text": "Amount of tax",
                            "translation": "세금 액수",
                        },
                        {
                            "id": "D",
                            "text": "Discount amount",
                            "translation": "할인 금액",
                        },
                    ],
                    "answer": "B",
                    "explanation": "'Subtotal'은 세전 합계를 의미한다.",
                },
            ],
        }
    ]

    # 10) Chart
    chart = [
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Chart",
                    "text": (
                        "Quarterly Revenue and Expenses (in $ thousands)\n\n"
                        "| Quarter | Revenue | Expenses | Net Profit |\n"
                        "|---------|---------|----------|------------|\n"
                        "|   Q1    |   85    |    62    |     23     |\n"
                        "|   Q2    |   92    |    70    |     22     |\n"
                        "|   Q3    |   88    |    65    |     23     |\n"
                        "|   Q4    |   95    |    74    |     21     |\n"
                        "\n"
                        "Notes:\n"
                        "- Q2 saw a significant increase in marketing expenses due to a new product launch.\n"
                        "- Q4 revenue was the highest, but net profit was the lowest due to increased year-end bonuses and facility upgrades.\n"
                        "- The company maintained steady profit margins in Q1 and Q3, despite minor fluctuations in revenue and expenses."
                    ),
                    "translation": (
                        "분기별 매출 및 비용 (천 달러 단위)\n\n"
                        "| 분기   | 매출 | 비용 | 순이익 |\n"
                        "|--------|------|------|--------|\n"
                        "| 1분기  |  85  |  62  |   23   |\n"
                        "| 2분기  |  92  |  70  |   22   |\n"
                        "| 3분기  |  88  |  65  |   23   |\n"
                        "| 4분기  |  95  |  74  |   21   |\n"
                        "\n"
                        "비고:\n"
                        "- 2분기는 신제품 출시로 마케팅 비용이 크게 증가함.\n"
                        "- 4분기는 매출이 가장 높았으나, 연말 보너스 및 시설 투자로 순이익이 가장 낮았음.\n"
                        "- 1, 3분기는 매출·비용 변동에도 불구하고 안정적인 이익률을 유지함."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "According to the chart, in which quarter did the company achieve the highest net profit?",
                    "questionTranslation": "표에 따르면 회사가 가장 높은 순이익을 기록한 분기는 언제입니까?",
                    "choices": [
                        {"id": "A", "text": "Q1", "translation": "1분기"},
                        {"id": "B", "text": "Q2", "translation": "2분기"},
                        {"id": "C", "text": "Q3", "translation": "3분기"},
                        {"id": "D", "text": "Q4", "translation": "4분기"},
                    ],
                    "answer": "A",
                    "explanation": "Q1과 Q3 모두 순이익 23이지만, Q1이 먼저이므로 Q1이 정답.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": (
                        "What can be inferred about the impact of increased expenses in Q4 on the company's profitability?"
                    ),
                    "questionTranslation": (
                        "4분기의 비용 증가가 회사의 수익성에 미친 영향에 대해 추론할 수 있는 것은 무엇입니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "Despite record-high revenue, net profit decreased due to higher expenses.",
                            "translation": "역대 최고 매출에도 불구하고 비용 증가로 순이익이 감소했다",
                        },
                        {
                            "id": "B",
                            "text": "Net profit increased along with revenue.",
                            "translation": "매출과 함께 순이익도 증가했다",
                        },
                        {
                            "id": "C",
                            "text": "Expenses had no effect on net profit.",
                            "translation": "비용이 순이익에 영향을 주지 않았다",
                        },
                        {
                            "id": "D",
                            "text": "The company had losses in Q4.",
                            "translation": "4분기에 적자를 기록했다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "비고에 매출은 최고였으나 비용 증가로 순이익이 가장 낮았다고 명시.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "어휘",
                    "questionText": "In the context of the chart, the word 'expenses' is closest in meaning to ____.",
                    "questionTranslation": "표의 맥락에서 'expenses'는 어떤 의미와 가장 가깝습니까?",
                    "choices": [
                        {"id": "A", "text": "costs", "translation": "비용"},
                        {"id": "B", "text": "profits", "translation": "이익"},
                        {"id": "C", "text": "assets", "translation": "자산"},
                        {"id": "D", "text": "sales", "translation": "매출"},
                    ],
                    "answer": "A",
                    "explanation": "'expenses'는 회사의 지출, 즉 비용을 의미한다.",
                },
            ],
        }
    ]

    # 11) Chat
    chat = [
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Chat",
                    "text": (
                        "Jin: Hi, everyone! Are we still meeting at 3 p.m. today?\n"
                        "Mina: Yes, but the meeting room has changed to B-204 because A-101 is being cleaned.\n"
                        "Alex: Got it. Should I bring the project proposal printouts?\n"
                        "Mina: I already printed the proposals, but can you bring the updated timeline?\n"
                        "Alex: Sure, I’ll bring both the timeline and the feedback summary from last week.\n"
                        "Jin: Thanks, Alex. Mina, do you want me to prepare the projector?\n"
                        "Mina: That would be great. Also, can you check if the Wi-Fi in B-204 is working? We’ll need it for the video call with the Seoul office.\n"
                        "Jin: I’ll check it before the meeting. Who’s joining remotely?\n"
                        "Mina: Ms. Park and Mr. Lee from Seoul, and possibly David from Busan if his schedule allows.\n"
                        "Alex: Should we send them the agenda in advance?\n"
                        "Mina: Yes, please email the agenda and the video call link to everyone by noon.\n"
                        "Jin: Will do. Anything else we need to prepare?\n"
                        "Mina: That’s all for now. See you all at 3 in B-204!"
                    ),
                    "translation": (
                        "진: 모두 안녕하세요! 오늘 오후 3시에 여전히 회의하나요?\n"
                        "미나: 네, 그런데 A-101호가 청소 중이라 회의실이 B-204호로 변경됐어요.\n"
                        "알렉스: 알겠습니다. 프로젝트 제안서 출력본을 가져갈까요?\n"
                        "미나: 제안서는 이미 출력했는데, 업데이트된 일정표를 가져올 수 있나요?\n"
                        "알렉스: 네, 일정표랑 지난주 피드백 요약도 같이 가져갈게요.\n"
                        "진: 고마워요, 알렉스. 미나, 제가 프로젝터 준비할까요?\n"
                        "미나: 네, 부탁해요. 그리고 B-204호 와이파이도 확인해줄 수 있나요? 서울 사무소랑 화상회의가 필요해요.\n"
                        "진: 회의 전에 확인할게요. 원격으로 참석하는 분은 누구죠?\n"
                        "미나: 서울에서 박 부장님과 이 과장님, 그리고 부산의 데이비드는 일정이 되면 참석할 거예요.\n"
                        "알렉스: 미리 안건을 보내드릴까요?\n"
                        "미나: 네, 모두에게 안건이랑 화상회의 링크를 정오까지 이메일로 보내주세요.\n"
                        "진: 알겠습니다. 준비할 것 더 있나요?\n"
                        "미나: 지금은 없어요. 3시에 B-204호에서 봬요!"
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "일치",
                    "questionText": "Which of the following is true about the meeting?",
                    "questionTranslation": "회의에 대해 옳은 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It will be held in Room A-101.",
                            "translation": "A-101호에서 열린다",
                        },
                        {
                            "id": "B",
                            "text": "Some participants will join remotely.",
                            "translation": "일부 참석자는 원격으로 참여한다",
                        },
                        {
                            "id": "C",
                            "text": "The meeting was cancelled.",
                            "translation": "회의가 취소되었다",
                        },
                        {
                            "id": "D",
                            "text": "No agenda will be sent.",
                            "translation": "안건이 발송되지 않는다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "서울과 부산에서 원격 참석자가 있다고 언급된다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What is Alex responsible for bringing to the meeting?",
                    "questionTranslation": "알렉스가 회의에 가져와야 하는 것은 무엇입니까?",
                    "choices": [
                        {"id": "A", "text": "Projector", "translation": "프로젝터"},
                        {
                            "id": "B",
                            "text": "Updated timeline and feedback summary",
                            "translation": "업데이트된 일정표와 피드백 요약",
                        },
                        {
                            "id": "C",
                            "text": "Wi-Fi router",
                            "translation": "와이파이 라우터",
                        },
                        {"id": "D", "text": "Budget file", "translation": "예산 파일"},
                    ],
                    "answer": "B",
                    "explanation": "알렉스는 일정표와 피드백 요약을 가져오기로 했다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "추론",
                    "questionText": "What can be inferred about Jin?",
                    "questionTranslation": "진에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "He is responsible for checking technical equipment.",
                            "translation": "기기 점검을 담당한다",
                        },
                        {
                            "id": "B",
                            "text": "He will join the meeting remotely.",
                            "translation": "원격으로 참석한다",
                        },
                        {
                            "id": "C",
                            "text": "He is preparing the feedback summary.",
                            "translation": "피드백 요약을 준비한다",
                        },
                        {
                            "id": "D",
                            "text": "He is not attending the meeting.",
                            "translation": "회의에 참석하지 않는다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "진은 프로젝터 준비와 와이파이 점검을 맡았다.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "세부사항",
                    "questionText": "By what time should the agenda and video call link be sent?",
                    "questionTranslation": "안건과 화상회의 링크는 언제까지 보내야 합니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "By 10 a.m.",
                            "translation": "오전 10시까지",
                        },
                        {"id": "B", "text": "By noon", "translation": "정오까지"},
                        {"id": "C", "text": "By 2 p.m.", "translation": "오후 2시까지"},
                        {"id": "D", "text": "By 3 p.m.", "translation": "오후 3시까지"},
                    ],
                    "answer": "B",
                    "explanation": "정오까지 이메일로 보내달라고 요청했다.",
                },
            ],
        }
    ]

    # 12) Report
    report = [
        {
            "part": 7,
            "difficulty": "Medium",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Report",
                    "text": (
                        "Monthly Sales Report – April 2025\n\n"
                        "Total sales revenue for April increased by 8% compared to March, reaching $120,000. This growth was primarily driven by a 15% rise in online orders, which accounted for nearly half of all sales. The launch of the spring promotional campaign on the website contributed to a significant boost in customer traffic and average order value. In contrast, revenue from brick-and-mortar stores remained flat at $62,000, with foot traffic showing little change from the previous month.\n\n"
                        "The best-selling product category was home electronics, followed by kitchen appliances and personal care items. Notably, the new wireless headphones introduced in early April quickly became a top seller online, while in-store sales of seasonal items such as fans and air purifiers lagged behind expectations. Customer feedback indicated high satisfaction with the online shopping experience, but several in-store shoppers mentioned long checkout lines and limited product displays as areas for improvement.\n\n"
                        "To maintain sales momentum, the report recommends expanding digital marketing efforts and introducing targeted in-store promotions. Additional staff training and improved store layouts may also help enhance the customer experience and drive higher in-store sales in the coming months."
                    ),
                    "translation": (
                        "월간 판매 보고서 – 2025년 4월\n\n"
                        "4월 총 매출은 3월 대비 8% 증가한 12만 달러를 기록했습니다. 이러한 성장은 온라인 주문이 15% 증가하며 전체 매출의 절반 가까이를 차지한 것이 주요 원인입니다. 웹사이트에서 진행된 봄 프로모션 캠페인이 고객 유입과 평균 주문 금액 증가에 크게 기여했습니다. 반면, 오프라인 매장 매출은 6만 2천 달러로 전월과 거의 변동이 없었으며, 방문 고객 수도 큰 변화가 없었습니다.\n\n"
                        "가장 많이 판매된 제품군은 가전제품이었고, 그 다음은 주방용품과 개인관리용품이었습니다. 특히 4월 초 출시된 무선 헤드폰은 온라인에서 빠르게 베스트셀러가 되었으나, 매장 내 계절상품(선풍기, 공기청정기 등) 판매는 기대에 미치지 못했습니다. 고객 피드백을 보면 온라인 쇼핑 경험에 대한 만족도가 높았으나, 오프라인 매장에서는 계산대 대기 시간과 한정된 상품 진열에 대한 개선 요청이 있었습니다.\n\n"
                        "판매 상승세 유지를 위해 디지털 마케팅 확대와 매장 내 타깃 프로모션 도입이 권장됩니다. 추가 직원 교육과 매장 레이아웃 개선도 고객 경험을 높이고 향후 오프라인 매출 증대에 도움이 될 것입니다."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "What is the main purpose of this report?",
                    "questionTranslation": "이 보고서의 주요 목적은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "To summarize monthly sales performance and suggest improvements",
                            "translation": "월간 판매 실적을 요약하고 개선 방안을 제시하기 위해",
                        },
                        {
                            "id": "B",
                            "text": "To announce a new product launch",
                            "translation": "신제품 출시를 알리기 위해",
                        },
                        {
                            "id": "C",
                            "text": "To compare competitor pricing",
                            "translation": "경쟁사 가격을 비교하기 위해",
                        },
                        {
                            "id": "D",
                            "text": "To recruit new staff",
                            "translation": "신규 직원을 채용하기 위해",
                        },
                    ],
                    "answer": "A",
                    "explanation": "보고서는 4월 판매 실적을 요약하고 향후 개선 방안을 제시한다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "According to the report, which product category had the highest sales in April?",
                    "questionTranslation": "보고서에 따르면 4월에 가장 많이 판매된 제품군은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Home electronics",
                            "translation": "가전제품",
                        },
                        {
                            "id": "B",
                            "text": "Kitchen appliances",
                            "translation": "주방용품",
                        },
                        {
                            "id": "C",
                            "text": "Personal care items",
                            "translation": "개인관리용품",
                        },
                        {
                            "id": "D",
                            "text": "Seasonal items",
                            "translation": "계절상품",
                        },
                    ],
                    "answer": "A",
                    "explanation": "본문에 home electronics가 가장 많이 판매된 제품군이라고 명시되어 있다.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "추론",
                    "questionText": "What can be inferred about in-store sales performance?",
                    "questionTranslation": "오프라인 매장 판매 실적에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It did not improve compared to March.",
                            "translation": "3월과 비교해 개선되지 않았다",
                        },
                        {
                            "id": "B",
                            "text": "It increased significantly due to new products.",
                            "translation": "신제품 덕분에 크게 증가했다",
                        },
                        {
                            "id": "C",
                            "text": "It was higher than online sales.",
                            "translation": "온라인 판매보다 높았다",
                        },
                        {
                            "id": "D",
                            "text": "It was negatively affected by staff shortages.",
                            "translation": "직원 부족으로 악영향을 받았다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "매장 매출은 'remained flat' 즉, 개선되지 않았다고 언급되어 있다.",
                },
            ],
        }
    ]

    # 13) Other
    other = [
        {
            "part": 7,
            "difficulty": "Easy",
            "questionSetType": "Single",
            "passages": [
                {
                    "seq": 1,
                    "type": "Other",
                    "text": (
                        "FAQ: Company Wellness Program\n\n"
                        "Q: Who is eligible?\n"
                        "A: All full-time employees.\n\n"
                        "Q: How do I sign up?\n"
                        "A: Complete the online form by May 31."
                    ),
                    "translation": (
                        "FAQ: 회사 웰니스 프로그램\n\n"
                        "Q: 누가 참여할 수 있습니까?\n"
                        "A: 모든 정규직 직원.\n\n"
                        "Q: 어떻게 신청합니까?\n"
                        "A: 5월 31일까지 온라인 양식을 작성하세요."
                    ),
                }
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "Who can participate in the wellness program?",
                    "questionTranslation": "웰니스 프로그램에 누가 참여할 수 있습니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Temporary staff",
                            "translation": "임시 직원",
                        },
                        {
                            "id": "B",
                            "text": "Full-time employees",
                            "translation": "정규직 직원",
                        },
                        {"id": "C", "text": "Contractors", "translation": "계약직"},
                        {"id": "D", "text": "Interns only", "translation": "인턴만"},
                    ],
                    "answer": "B",
                    "explanation": "FAQ 첫 번째 항목에서 모든 정규직 직원이라고 명시한다.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "참조",
                    "questionText": "What does the word 'form' in the second answer refer to?",
                    "questionTranslation": "두 번째 답변에서 'form'은 무엇을 가리킵니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A printed brochure",
                            "translation": "인쇄된 브로셔",
                        },
                        {
                            "id": "B",
                            "text": "An online application",
                            "translation": "온라인 신청서",
                        },
                        {
                            "id": "C",
                            "text": "A physical examination",
                            "translation": "건강 검진",
                        },
                        {
                            "id": "D",
                            "text": "A gym membership",
                            "translation": "헬스장 회원권",
                        },
                    ],
                    "answer": "B",
                    "explanation": "FAQ에서 온라인 양식을 작성하라고 안내한다.",
                },
            ],
        }
    ]


class Part7DoublePassageFewShotExamples:
    """
    TOEIC Part 7 double-passage few-shot examples
    ─ 대표 조합: Email+Reply, Advertisement+Inquiry Email, Article+Letter, Form+Notice 등 ─
    """

    # 1) Email + Reply
    email_reply = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Double",
            "passages": [
                {
                    "seq": 1,
                    "type": "Email",
                    "text": (
                        "Subject: Request for Meeting Room Reservation and Equipment\n\n"
                        "Dear Facilities Team,\n\n"
                        "I am writing to request a reservation for the main conference room on May 28 from 2 p.m. to 4 p.m. for an important client presentation. "
                        "We expect approximately 20 attendees, including several executives from our client’s company. In addition to the room, we will need a projector, a whiteboard with markers, and access to the video conferencing system, as two participants will be joining remotely from our Busan office.\n\n"
                        "Please confirm whether the room and requested equipment are available at the specified time. If possible, I would also appreciate having bottled water and notepads prepared for all attendees. "
                        "If there are any forms or procedures I need to complete in advance, kindly let me know.\n\n"
                        "Thank you for your assistance.\n"
                        "Best regards,\n"
                        "John Lee\n"
                        "Sales Department"
                    ),
                    "translation": (
                        "제목: 회의실 및 장비 예약 요청\n\n"
                        "시설팀 귀하,\n\n"
                        "5월 28일 오후 2시부터 4시까지 메인 회의실을 중요한 고객 프레젠테이션 용도로 예약하고자 합니다. "
                        "참석자는 약 20명이며, 고객사 임원도 여러 명 포함되어 있습니다. 회의실 외에 프로젝터, 마커가 구비된 화이트보드, "
                        "그리고 부산 사무소에서 원격으로 참석할 2명을 위한 화상회의 시스템도 필요합니다.\n\n"
                        "해당 시간에 회의실과 요청 장비 사용이 가능한지 확인 부탁드립니다. 가능하다면 참석자 전원에게 생수와 노트도 준비해주시면 감사하겠습니다. "
                        "사전에 작성해야 할 양식이나 절차가 있다면 안내 부탁드립니다.\n\n"
                        "협조에 감사드립니다.\n"
                        "영업부 John Lee"
                    ),
                },
                {
                    "seq": 2,
                    "type": "Reply Email",
                    "text": (
                        "Subject: Re: Request for Meeting Room Reservation and Equipment\n\n"
                        "Dear Mr. Lee,\n\n"
                        "Thank you for your detailed request. The main conference room is available on May 28 from 2 p.m. to 4 p.m., and I have reserved it under your name. "
                        "A projector and whiteboard with markers will be set up as requested. Our IT team will ensure the video conferencing system is tested and ready for your remote participants from Busan.\n\n"
                        "Bottled water and notepads will be provided for all attendees. Please note that food catering is not included, but you may arrange it separately if needed. "
                        "For security purposes, please send us a list of external visitors by May 26. Attached is the facility use form; kindly complete and return it at least one day before your event.\n\n"
                        "If you have any additional requirements or changes, let us know as soon as possible. We look forward to supporting your successful meeting.\n\n"
                        "Best regards,\n"
                        "Sophie Kim\n"
                        "Facilities Team"
                    ),
                    "translation": (
                        "제목: 회의실 및 장비 예약 요청 관련\n\n"
                        "Lee 님께,\n\n"
                        "상세한 요청 사항을 보내주셔서 감사합니다. 메인 회의실은 5월 28일 오후 2시~4시에 사용 가능하며, 귀하 명의로 예약해 두었습니다. "
                        "요청하신 프로젝터와 마커가 구비된 화이트보드도 준비하겠습니다. IT팀이 부산 원격 참석자를 위한 화상회의 시스템도 사전에 점검할 예정입니다.\n\n"
                        "모든 참석자에게 생수와 노트가 제공됩니다. 다만, 식음료 케이터링은 포함되어 있지 않으니 필요 시 별도 준비 부탁드립니다. "
                        "보안상 외부 방문자 명단을 5월 26일까지 보내주시기 바랍니다. 시설 이용 신청서를 첨부하오니, 행사 하루 전까지 작성해 회신해 주십시오.\n\n"
                        "추가 요청이나 변경 사항이 있으면 최대한 빨리 알려주시기 바랍니다. 성공적인 회의가 되도록 지원하겠습니다.\n\n"
                        "감사합니다.\n"
                        "시설팀 Sophie Kim"
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "What equipment did Mr. Lee request for the meeting?",
                    "questionTranslation": "Lee 씨가 회의에 요청한 장비는 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Projector, whiteboard, and video conferencing system",
                            "translation": "프로젝터, 화이트보드, 화상회의 시스템",
                        },
                        {
                            "id": "B",
                            "text": "Printer and scanner",
                            "translation": "프린터와 스캐너",
                        },
                        {
                            "id": "C",
                            "text": "Microphone and speakers only",
                            "translation": "마이크와 스피커만",
                        },
                        {
                            "id": "D",
                            "text": "Laptop computers",
                            "translation": "노트북 컴퓨터",
                        },
                    ],
                    "answer": "A",
                    "explanation": "본문에 세 가지 장비 모두 요청한 내용이 명시되어 있음.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What must Mr. Lee do before the meeting date?",
                    "questionTranslation": "회의 전까지 Lee 씨가 해야 할 일은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Return the facility use form and send a list of external visitors",
                            "translation": "시설 이용 신청서 제출 및 외부 방문자 명단 송부",
                        },
                        {
                            "id": "B",
                            "text": "Pay a reservation fee",
                            "translation": "예약비 결제",
                        },
                        {
                            "id": "C",
                            "text": "Arrange food catering through facilities team",
                            "translation": "시설팀을 통해 케이터링 신청",
                        },
                        {
                            "id": "D",
                            "text": "Test the video system himself",
                            "translation": "직접 화상 시스템 점검",
                        },
                    ],
                    "answer": "A",
                    "explanation": "회신에 두 가지 모두 요청되어 있음.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "정보연계",
                    "questionText": "Which of the following arrangements is confirmed in the reply but was not explicitly requested in the original email?",
                    "questionTranslation": "회신에서 확정되었으나 원래 이메일에서 명시적으로 요청되지 않은 준비 사항은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Notepads for attendees",
                            "translation": "참석자용 노트",
                        },
                        {"id": "B", "text": "Projector", "translation": "프로젝터"},
                        {"id": "C", "text": "Whiteboard", "translation": "화이트보드"},
                        {
                            "id": "D",
                            "text": "Video conferencing system",
                            "translation": "화상회의 시스템",
                        },
                    ],
                    "answer": "A",
                    "explanation": "원본 이메일에서는 'notepads'는 'appreciate' 수준의 요청(가능하다면)으로만 언급, 회신에서 확정적으로 제공한다고 명시됨.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "세부사항",
                    "questionText": "What is NOT included in the facilities team’s arrangements?",
                    "questionTranslation": "시설팀이 준비하지 않는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Food catering",
                            "translation": "식음료 케이터링",
                        },
                        {"id": "B", "text": "Projector", "translation": "프로젝터"},
                        {"id": "C", "text": "Whiteboard", "translation": "화이트보드"},
                        {"id": "D", "text": "Bottled water", "translation": "생수"},
                    ],
                    "answer": "A",
                    "explanation": "케이터링은 별도 준비해야 한다고 회신에 명시됨.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "참조",
                    "questionText": "In the reply, what does 'it' in 'I have reserved it under your name' refer to?",
                    "questionTranslation": "회신에서 'I have reserved it under your name'의 'it'은 무엇을 가리킵니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "The main conference room",
                            "translation": "메인 회의실",
                        },
                        {"id": "B", "text": "The projector", "translation": "프로젝터"},
                        {
                            "id": "C",
                            "text": "The video conferencing system",
                            "translation": "화상회의 시스템",
                        },
                        {"id": "D", "text": "The bottled water", "translation": "생수"},
                    ],
                    "answer": "A",
                    "explanation": "'it'은 메인 회의실을 의미함.",
                },
            ],
        }
    ]

    # 2) Advertisement + Inquiry Email
    advertisement_inquiry = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Double",
            "passages": [
                {
                    "seq": 1,
                    "type": "Advertisement",
                    "text": (
                        "**Grand Opening—Sunrise Café**\n\n"
                        "Celebrate the grand opening of Sunrise Café on June 10! From 8 a.m. to 10 a.m., enjoy complimentary coffee and a selection of pastries, including croissants, muffins, and fruit tarts. "
                        "The first 50 customers will receive a free reusable mug. Sunrise Café features locally roasted coffee, vegan and gluten-free pastry options, and a cozy reading corner with free Wi-Fi. "
                        "Special opening day offer: All drinks are 20% off until noon. Located at 123 Maple Street, across from City Park. Parking is available behind the building.\n\n"
                        "Open daily: 7 a.m.–7 p.m.\nContact: (555) 987-6543\nFollow us on Instagram @sunrisecafe"
                    ),
                    "translation": (
                        "**그랜드 오프닝—선라이즈 카페**\n\n"
                        "6월 10일 선라이즈 카페 오픈 행사에 초대합니다! 오전 8시~10시 무료 커피와 다양한 페이스트리(크루아상, 머핀, 과일 타르트 등) 제공, "
                        "선착순 50명에게는 리유저블 머그컵 증정. 선라이즈 카페는 로컬 로스팅 커피, 비건 및 글루텐 프리 페이스트리, 무료 와이파이가 있는 아늑한 독서 공간을 갖추고 있습니다. "
                        "오프닝 당일 특별 혜택: 정오까지 모든 음료 20% 할인. 위치: 시티파크 맞은편 메이플가 123번지. 건물 뒤 주차장 이용 가능.\n\n"
                        "영업시간: 매일 오전 7시~오후 7시\n문의: (555) 987-6543\n인스타그램 @sunrisecafe"
                    ),
                },
                {
                    "seq": 2,
                    "type": "Inquiry Email",
                    "text": (
                        "Subject: Questions about Grand Opening Event\n\n"
                        "Hello,\n\n"
                        "I saw your advertisement for the grand opening and am excited to visit. I have a few questions:\n"
                        "1. Will there be any vegan or gluten-free pastry options available during the complimentary breakfast?\n"
                        "2. Is the free mug offer limited to one per group or per person?\n"
                        "3. Can I reserve a table in advance for a group of six?\n"
                        "4. Is parking free for customers?\n"
                        "Thank you for your help.\n"
                        "Best regards,\nMina Park"
                    ),
                    "translation": (
                        "제목: 오프닝 행사 관련 문의\n\n"
                        "안녕하세요.\n\n"
                        "그랜드 오프닝 광고를 보고 방문할 예정입니다. 몇 가지 궁금한 점이 있습니다:\n"
                        "1. 무료 조식 시간에 비건 또는 글루텐 프리 페이스트리가 제공되나요?\n"
                        "2. 머그컵 증정은 1인 1개인가요, 아니면 일행당 1개인가요?\n"
                        "3. 6인 단체 테이블을 미리 예약할 수 있나요?\n"
                        "4. 주차장은 무료인가요?\n"
                        "답변 부탁드립니다.\n"
                        "감사합니다.\n박미나"
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "According to the advertisement, what special offer is available until noon on opening day?",
                    "questionTranslation": "광고에 따르면 오프닝 당일 정오까지 제공되는 특별 혜택은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "20% off all drinks",
                            "translation": "모든 음료 20% 할인",
                        },
                        {
                            "id": "B",
                            "text": "Free lunch for all customers",
                            "translation": "모든 고객 무료 점심",
                        },
                        {
                            "id": "C",
                            "text": "Buy one get one free pastries",
                            "translation": "페이스트리 1+1",
                        },
                        {
                            "id": "D",
                            "text": "Free coffee all day",
                            "translation": "하루 종일 무료 커피",
                        },
                    ],
                    "answer": "A",
                    "explanation": "광고에 정오까지 모든 음료 20% 할인 명시.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What is Mina Park specifically asking about regarding the free mug offer?",
                    "questionTranslation": "박미나 씨가 머그컵 증정에 대해 구체적으로 문의한 내용은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "If the mug is reusable",
                            "translation": "머그컵이 리유저블인지",
                        },
                        {
                            "id": "B",
                            "text": "Whether the offer is per person or per group",
                            "translation": "1인 1개인지, 일행당 1개인지",
                        },
                        {
                            "id": "C",
                            "text": "If the mug can be reserved",
                            "translation": "머그컵 예약 가능 여부",
                        },
                        {
                            "id": "D",
                            "text": "If the mug is available after 10 a.m.",
                            "translation": "오전 10시 이후에도 증정되는지",
                        },
                    ],
                    "answer": "B",
                    "explanation": "이메일 2번 항목에서 1인 1개인지, 일행당 1개인지 문의.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "정보연계",
                    "questionText": "Based on both the advertisement and the inquiry email, what can be inferred about the availability of vegan and gluten-free pastries during the complimentary breakfast?",
                    "questionTranslation": "광고와 문의 이메일을 종합할 때, 무료 조식 시간에 비건 및 글루텐 프리 페이스트리 제공 여부에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "They are definitely included, as stated in the ad.",
                            "translation": "광고에 명시되어 반드시 제공된다",
                        },
                        {
                            "id": "B",
                            "text": "They may be available, but Mina is seeking confirmation.",
                            "translation": "제공될 수 있으나, 미나가 확인을 요청하고 있다",
                        },
                        {
                            "id": "C",
                            "text": "They are not available at all.",
                            "translation": "전혀 제공되지 않는다",
                        },
                        {
                            "id": "D",
                            "text": "Only gluten-free options are available.",
                            "translation": "글루텐 프리만 제공된다",
                        },
                    ],
                    "answer": "B",
                    "explanation": "광고에 옵션이 있다고 언급되나, 미나가 실제 무료 조식에 포함되는지 확인 요청.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "정보연계",
                    "questionText": "If Mina wants to visit with five friends and receive a free mug for each person, what should she do based on the information in both passages?",
                    "questionTranslation": "미나가 친구 5명과 방문해 모두 머그컵을 받으려면, 두 지문 정보를 종합할 때 어떻게 해야 합니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Arrive early, as the offer is for the first 50 customers and clarify if it is per person.",
                            "translation": "일찍 도착하고, 1인 1개 증정 여부를 확인해야 한다",
                        },
                        {
                            "id": "B",
                            "text": "Reserve mugs in advance by phone.",
                            "translation": "전화로 미리 머그컵을 예약한다",
                        },
                        {
                            "id": "C",
                            "text": "Visit after 10 a.m. for the offer.",
                            "translation": "오전 10시 이후 방문한다",
                        },
                        {
                            "id": "D",
                            "text": "Purchase mugs at a discount.",
                            "translation": "할인된 가격에 머그컵을 구매한다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "광고에 선착순 50명, 이메일에 1인 1개 여부 문의. 모두 받으려면 일찍 도착하고 조건을 확인해야 함.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "세부사항",
                    "questionText": "According to the advertisement, which of the following is true about parking at Sunrise Café?",
                    "questionTranslation": "광고에 따르면 선라이즈 카페 주차에 대해 옳은 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Parking is available behind the building.",
                            "translation": "건물 뒤에 주차장이 있다",
                        },
                        {
                            "id": "B",
                            "text": "Parking is not available.",
                            "translation": "주차장이 없다",
                        },
                        {
                            "id": "C",
                            "text": "Parking is only for staff.",
                            "translation": "직원 전용 주차장이다",
                        },
                        {
                            "id": "D",
                            "text": "Parking is free for groups of six or more.",
                            "translation": "6인 이상 단체만 무료 주차 가능",
                        },
                    ],
                    "answer": "A",
                    "explanation": "광고에 건물 뒤 주차장 안내가 명시됨.",
                },
            ],
        }
    ]

    # 3) Article + Letter
    article_letter = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Double",
            "passages": [
                {
                    "seq": 1,
                    "type": "Article",
                    "text": (
                        "City Library Launches New Digital Service\n\n"
                        "The Central City Library has introduced a new digital lending platform, allowing members to borrow e-books and audiobooks remotely. "
                        "The service is available 24/7 and can be accessed via the library’s website or mobile app. Library officials hope the new system will increase access to resources for all residents.\n\n"
                        "In addition to the digital lending platform, the library has expanded its online catalog to include over 10,000 titles in multiple languages, as well as a selection of magazines and newspapers. "
                        "Members can place holds on popular titles and receive notifications when items become available. The library also offers virtual workshops on topics such as digital literacy, research skills, and creative writing, which are free for all members.\n\n"
                        "To promote the new service, the library is hosting a Digital Access Week from May 15 to May 21. During this event, staff will provide one-on-one assistance to help users set up their accounts and learn how to use the platform. "
                        "Participants who borrow at least two digital items during the week will be entered into a prize drawing for a new e-reader. For more information, visit the library’s website or contact the help desk."
                    ),
                    "translation": (
                        "시립 도서관, 신규 디지털 서비스 개시\n\n"
                        "중앙 시립 도서관이 전자책 및 오디오북을 원격으로 대여할 수 있는 디지털 플랫폼을 도입했습니다. "
                        "이 서비스는 연중무휴 24시간 이용 가능하며, 도서관 웹사이트 또는 모바일 앱을 통해 접속할 수 있습니다. 도서관 측은 이번 시스템이 모든 시민의 자료 접근성을 높일 것으로 기대하고 있습니다.\n\n"
                        "디지털 대출 플랫폼 외에도, 도서관은 온라인 카탈로그를 다국어 1만여 권 이상의 도서와 다양한 잡지, 신문으로 확장했습니다. "
                        "회원은 인기 도서에 예약을 걸고, 대출 가능 시 알림을 받을 수 있습니다. 또한 디지털 리터러시, 연구 스킬, 창작 글쓰기 등 다양한 주제의 온라인 워크숍도 무료로 제공합니다.\n\n"
                        "신규 서비스 홍보를 위해 도서관은 5월 15일부터 21일까지 '디지털 접근 주간'을 개최합니다. 이 기간 동안 직원이 계정 설정 및 플랫폼 사용법을 1:1로 안내하며, "
                        "주간 내 디지털 자료를 2권 이상 대출한 참가자에게는 전자책 리더기 추첨 기회가 주어집니다. 자세한 내용은 도서관 웹사이트 또는 안내 데스크에 문의하세요."
                    ),
                },
                {
                    "seq": 2,
                    "type": "Letter",
                    "text": (
                        "May 22, 2025\n\n"
                        "Dear Library Director,\n\n"
                        "I am a long-time member of the Central City Library and wanted to thank you for launching the new digital lending service. "
                        "It has made it much easier for me to access books, especially since I travel frequently for work. I was also able to join the creative writing workshop online last week, which I found very inspiring.\n\n"
                        "However, I had some difficulty setting up my account at first, and I noticed that some popular titles have long wait times. "
                        "I appreciate the staff’s assistance during Digital Access Week, but I hope the library will consider increasing the number of available copies for high-demand books in the future.\n\n"
                        "Thank you again for your efforts to modernize the library and support members like me who rely on digital resources.\n\n"
                        "Sincerely,\nAlex Kim"
                    ),
                    "translation": (
                        "2025년 5월 22일\n\n"
                        "도서관장님께,\n\n"
                        "저는 중앙 시립 도서관의 오랜 회원으로, 신규 디지털 대출 서비스 도입에 감사드립니다. "
                        "특히 업무상 자주 출장을 다니는 저에게 책을 쉽게 이용할 수 있게 되어 매우 편리합니다. 지난주에는 온라인 창작 글쓰기 워크숍에도 참여했는데, 매우 영감을 받았습니다.\n\n"
                        "다만, 계정 설정에 처음에 약간 어려움이 있었고, 인기 도서의 경우 대기 시간이 길다는 점이 아쉬웠습니다. "
                        "디지털 접근 주간에 직원분들의 도움을 받아 감사했지만, 앞으로 인기 도서의 대출 가능 권수를 늘려주시면 좋겠습니다.\n\n"
                        "도서관 현대화를 위해 힘써주신 점과 저처럼 디지털 자료에 의존하는 회원을 지원해주셔서 다시 한 번 감사드립니다.\n\n"
                        "감사합니다.\n김알렉스"
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "주제/목적",
                    "questionText": "What is the main topic of the article?",
                    "questionTranslation": "기사의 주요 내용은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A new digital lending service and related programs",
                            "translation": "신규 디지털 대출 서비스 및 관련 프로그램",
                        },
                        {
                            "id": "B",
                            "text": "Library renovation",
                            "translation": "도서관 리노베이션",
                        },
                        {
                            "id": "C",
                            "text": "Book donation event",
                            "translation": "도서 기부 행사",
                        },
                        {
                            "id": "D",
                            "text": "Staff recruitment",
                            "translation": "직원 채용",
                        },
                    ],
                    "answer": "A",
                    "explanation": "신규 디지털 대출 서비스와 온라인 워크숍, 이벤트 등 관련 프로그램이 기사 주제임.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "추론",
                    "questionText": "What can be inferred about Alex Kim?",
                    "questionTranslation": "김알렉스에 대해 추론할 수 있는 것은?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "He rarely visits the library in person.",
                            "translation": "직접 도서관 방문이 드물다",
                        },
                        {
                            "id": "B",
                            "text": "He works at the library.",
                            "translation": "도서관 직원이다",
                        },
                        {
                            "id": "C",
                            "text": "He prefers printed books.",
                            "translation": "종이책을 선호한다",
                        },
                        {
                            "id": "D",
                            "text": "He is a new member.",
                            "translation": "신규 회원이다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "출장이 잦아 원격 대출이 편리하다고 언급함.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "세부사항",
                    "questionText": "How can members access the new service?",
                    "questionTranslation": "회원들은 신규 서비스를 어떻게 이용할 수 있습니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Through the website or app",
                            "translation": "웹사이트 또는 앱을 통해",
                        },
                        {"id": "B", "text": "By phone only", "translation": "전화로만"},
                        {
                            "id": "C",
                            "text": "At the front desk",
                            "translation": "도서관 데스크에서",
                        },
                        {"id": "D", "text": "By mail", "translation": "우편으로"},
                    ],
                    "answer": "A",
                    "explanation": "웹사이트/앱을 통한 이용이 기사에 명시됨.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "정보연계",
                    "questionText": "What is one issue Alex Kim experienced that is also mentioned in the article?",
                    "questionTranslation": "김알렉스가 겪은 문제 중 기사에서도 언급된 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Difficulty setting up an account",
                            "translation": "계정 설정의 어려움",
                        },
                        {
                            "id": "B",
                            "text": "Problems with overdue fines",
                            "translation": "연체료 문제",
                        },
                        {
                            "id": "C",
                            "text": "Lack of audiobooks",
                            "translation": "오디오북 부족",
                        },
                        {
                            "id": "D",
                            "text": "Limited library hours",
                            "translation": "제한된 도서관 운영 시간",
                        },
                    ],
                    "answer": "A",
                    "explanation": "기사에서 계정 설정 지원(1:1 안내) 언급, 편지에서도 계정 설정이 어렵다고 언급.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "정보연계",
                    "questionText": "Based on both passages, what can be inferred about the popularity of the new digital service?",
                    "questionTranslation": "두 지문을 종합할 때, 신규 디지털 서비스의 인기에 대해 추론할 수 있는 것은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "It is popular, as there are long wait times for some titles.",
                            "translation": "일부 도서 대기 시간이 길어 인기가 많다",
                        },
                        {
                            "id": "B",
                            "text": "Few members are using it.",
                            "translation": "이용자가 거의 없다",
                        },
                        {
                            "id": "C",
                            "text": "It is only used by staff.",
                            "translation": "직원만 사용한다",
                        },
                        {
                            "id": "D",
                            "text": "It is only available during business hours.",
                            "translation": "영업시간에만 이용 가능하다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "편지에서 인기 도서 대기 시간 언급, 기사에서 대출 예약·알림 기능 언급 → 이용자 많아 대기 발생 추론 가능.",
                },
            ],
        }
    ]

    # 4) Form + Notice
    form_notice = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Double",
            "passages": [
                {
                    "seq": 1,
                    "type": "Form",
                    "text": (
                        "International Leadership Summit 2025 — Registration Form\n\n"
                        "Full Name: _______________________________\n"
                        "Organization: _____________________________\n"
                        "Job Title: ________________________________\n"
                        "Email Address: ____________________________\n"
                        "Phone Number: _____________________________\n"
                        "Country: _________________________________\n"
                        "\n"
                        "Session Preferences (Select up to 2):\n"
                        "  □ A. Global Business Trends\n"
                        "  □ B. Innovation in Leadership\n"
                        "  □ C. Diversity & Inclusion\n"
                        "  □ D. Digital Transformation\n"
                        "\n"
                        "Workshop Participation (Choose one):\n"
                        "  □ Morning (9:00–12:00)   □ Afternoon (14:00–17:00)\n"
                        "\n"
                        "Dietary Restrictions (Check all that apply):\n"
                        "  □ Vegetarian   □ Vegan   □ Gluten-Free   □ No Preference\n"
                        "\n"
                        "Special Assistance Needed? (Please specify): __________________________\n"
                        "\n"
                        "Networking Lunch (12:00–13:30):\n"
                        "  □ Will attend   □ Will not attend\n"
                        "\n"
                        "Payment Method:\n"
                        "  □ Credit Card   □ Bank Transfer   □ On-site Payment\n"
                        "\n"
                        "Signature: ____________________   Date: _______________\n"
                        "\n"
                        "Note: Registration closes May 31. Early registrants receive a welcome kit and priority seating."
                    ),
                    "translation": (
                        "국제 리더십 서밋 2025 — 등록 양식\n\n"
                        "성명: _______________________________\n"
                        "소속: _______________________________\n"
                        "직책: _______________________________\n"
                        "이메일 주소: _________________________\n"
                        "전화번호: ____________________________\n"
                        "국가: _______________________________\n"
                        "\n"
                        "세션 선호도 (최대 2개 선택):\n"
                        "  □ A. 글로벌 비즈니스 트렌드\n"
                        "  □ B. 리더십 혁신\n"
                        "  □ C. 다양성 및 포용\n"
                        "  □ D. 디지털 전환\n"
                        "\n"
                        "워크숍 참여 (하나 선택):\n"
                        "  □ 오전 (9:00–12:00)   □ 오후 (14:00–17:00)\n"
                        "\n"
                        "식이 제한 (해당 사항 모두 체크):\n"
                        "  □ 채식   □ 비건   □ 글루텐 프리   □ 무관\n"
                        "\n"
                        "특별 지원 필요 여부 (구체적으로 기재): __________________________\n"
                        "\n"
                        "네트워킹 점심 (12:00–13:30):\n"
                        "  □ 참석   □ 불참\n"
                        "\n"
                        "결제 방법:\n"
                        "  □ 신용카드   □ 계좌이체   □ 현장 결제\n"
                        "\n"
                        "서명: ____________________   날짜: _______________\n"
                        "\n"
                        "참고: 등록 마감은 5월 31일입니다. 선착순 등록자에게는 웰컴 키트와 우선 좌석이 제공됩니다."
                    ),
                },
                {
                    "seq": 2,
                    "type": "Notice",
                    "text": (
                        "**Notice to All Summit Participants**\n\n"
                        "Thank you for registering for the International Leadership Summit 2025. Please submit your completed registration form and payment by May 31. "
                        "Participants who attend both a morning and an afternoon workshop will receive a certificate of completion. "
                        "The networking lunch is complimentary for those who select 'Will attend' on the form. If you have dietary restrictions, indicate them clearly to ensure appropriate meal arrangements. "
                        "Special assistance (e.g., wheelchair access, sign language interpretation) can be requested in the relevant section of the form. "
                        "A confirmation email with your session assignments and further event details will be sent by June 5. "
                        "For questions, contact summit@leadershipconf.org or call (555) 321-7890."
                    ),
                    "translation": (
                        "**서밋 참가자 안내**\n\n"
                        "국제 리더십 서밋 2025에 등록해 주셔서 감사합니다. 등록 양식과 결제는 5월 31일까지 제출해 주시기 바랍니다. "
                        "오전과 오후 워크숍 모두 참석한 참가자에게는 수료증이 제공됩니다. 네트워킹 점심은 양식에서 '참석'을 선택한 분께 무료로 제공됩니다. "
                        "식이 제한이 있는 경우 반드시 양식에 명확히 기재해 주시기 바랍니다. "
                        "특별 지원(예: 휠체어 접근, 수화 통역 등)이 필요한 경우 해당란에 요청해 주세요. "
                        "세션 배정 및 행사 세부 안내는 6월 5일까지 이메일로 발송됩니다. "
                        "문의: summit@leadershipconf.org 또는 (555) 321-7890"
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "Who will receive a certificate of completion at the summit?",
                    "questionTranslation": "서밋에서 수료증을 받는 사람은 누구입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "All registrants",
                            "translation": "모든 등록자",
                        },
                        {
                            "id": "B",
                            "text": "Those who attend both a morning and an afternoon workshop",
                            "translation": "오전과 오후 워크숍 모두 참석자",
                        },
                        {
                            "id": "C",
                            "text": "Only keynote speakers",
                            "translation": "기조연설자만",
                        },
                        {
                            "id": "D",
                            "text": "Participants with dietary restrictions",
                            "translation": "식이 제한이 있는 참가자",
                        },
                    ],
                    "answer": "B",
                    "explanation": "안내문에 오전·오후 워크숍 모두 참석자에게 수료증 제공 명시.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What must participants do by May 31?",
                    "questionTranslation": "참가자는 5월 31일까지 무엇을 해야 합니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Submit the registration form and payment",
                            "translation": "등록 양식과 결제 제출",
                        },
                        {
                            "id": "B",
                            "text": "Select their lunch menu",
                            "translation": "점심 메뉴 선택",
                        },
                        {
                            "id": "C",
                            "text": "Attend a workshop",
                            "translation": "워크숍 참석",
                        },
                        {
                            "id": "D",
                            "text": "Send a feedback survey",
                            "translation": "설문조사 제출",
                        },
                    ],
                    "answer": "A",
                    "explanation": "등록 양식과 결제 모두 5월 31일까지 제출해야 함.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "세부사항",
                    "questionText": "How can participants request special assistance for the event?",
                    "questionTranslation": "참가자가 특별 지원을 요청하려면 어떻게 해야 합니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Call the admin office only",
                            "translation": "행정실에 전화만 한다",
                        },
                        {
                            "id": "B",
                            "text": "Indicate in the relevant section of the form",
                            "translation": "양식 해당란에 기재한다",
                        },
                        {
                            "id": "C",
                            "text": "Send a separate letter",
                            "translation": "별도 편지를 보낸다",
                        },
                        {
                            "id": "D",
                            "text": "No action is needed",
                            "translation": "별도 조치 불필요",
                        },
                    ],
                    "answer": "B",
                    "explanation": "안내문에 양식 해당란에 요청하라고 명시.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "정보연계",
                    "questionText": "If a participant selects 'Will attend' for the networking lunch but does NOT indicate any dietary restrictions, what meal arrangements will be made?",
                    "questionTranslation": "'네트워킹 점심'에 '참석'을 선택했으나 식이 제한을 기재하지 않은 참가자에게는 어떤 식사가 제공됩니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A standard meal will be provided",
                            "translation": "일반 식사가 제공된다",
                        },
                        {
                            "id": "B",
                            "text": "No meal will be provided",
                            "translation": "식사가 제공되지 않는다",
                        },
                        {
                            "id": "C",
                            "text": "A vegan meal will be provided",
                            "translation": "비건 식사가 제공된다",
                        },
                        {
                            "id": "D",
                            "text": "They must bring their own meal",
                            "translation": "직접 식사를 준비해야 한다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "식이 제한 미기재 시 일반 식사가 제공됨.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "정보연계",
                    "questionText": "Based on both the form and the notice, what is the benefit of registering early?",
                    "questionTranslation": "양식과 안내문을 종합할 때, 선착순 등록자의 혜택은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Discounted registration fee",
                            "translation": "등록비 할인",
                        },
                        {
                            "id": "B",
                            "text": "Welcome kit and priority seating",
                            "translation": "웰컴 키트 및 우선 좌석",
                        },
                        {
                            "id": "C",
                            "text": "Free hotel accommodation",
                            "translation": "무료 호텔 숙박",
                        },
                        {
                            "id": "D",
                            "text": "Private meeting with keynote speakers",
                            "translation": "기조연설자와의 개별 미팅",
                        },
                    ],
                    "answer": "B",
                    "explanation": "양식 하단에 선착순 등록자에게 웰컴 키트와 우선 좌석 제공 명시.",
                },
            ],
        }
    ]


class Part7TriplePassageFewShotExamples:
    """
    TOEIC Part 7 triple-passage few-shot examples
    ─ 대표 조합: Email+Schedule+Notice, Chat+Article+Form 등 ─
    """

    # 1) Email + Schedule + Notice
    email_schedule_notice = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Triple",
            "passages": [
                {
                    "seq": 1,
                    "type": "Email",
                    "text": (
                        "Subject: Project Phoenix Kickoff – Final Details & Schedule\n\n"
                        "Dear Team,\n\n"
                        "We are excited to announce that the official kickoff meeting for Project Phoenix will be held on June 3. Please review the detailed schedule below and note your assigned session locations. "
                        "All team members are expected to participate in both the morning and afternoon sessions. If you have any dietary restrictions or require special assistance, reply to this email by May 30.\n\n"
                        "Additionally, please prepare a brief self-introduction and bring your completed onboarding forms. For those joining remotely, a video call link will be sent the day before the meeting. "
                        "If you have questions about the agenda or logistics, contact the admin office or reply directly to this message.\n\n"
                        "Looking forward to a productive start!\n\n"
                        "Best regards,\n"
                        "Soojin Park\n"
                        "Project Manager"
                    ),
                    "translation": (
                        "제목: 프로젝트 피닉스 킥오프 – 최종 안내 및 일정\n\n"
                        "팀 여러분,\n\n"
                        "프로젝트 피닉스의 공식 킥오프 미팅이 6월 3일에 개최됩니다. 아래 상세 일정을 확인하시고, 각 세션별 배정된 장소를 반드시 숙지해 주세요. "
                        "모든 팀원은 오전과 오후 세션 모두 참석해야 합니다. 식이 제한이나 특별 지원이 필요한 경우 5월 30일까지 이 메일로 회신 바랍니다.\n\n"
                        "또한 간단한 자기소개를 준비하고, 온보딩 서류를 작성해 오시기 바랍니다. 원격 참석자는 전날 화상회의 링크를 별도 안내드릴 예정입니다. "
                        "의제나 행사 관련 문의는 행정실 또는 본 메일로 회신해 주세요.\n\n"
                        "힘찬 출발을 기대합니다!\n\n"
                        "감사합니다.\n"
                        "박수진 드림\n"
                        "프로젝트 매니저"
                    ),
                },
                {
                    "seq": 2,
                    "type": "Schedule",
                    "text": (
                        "Project Phoenix Kickoff – Detailed Schedule\n\n"
                        "08:40–09:00  Registration & Coffee (Lobby)\n"
                        "09:00–09:30  Welcome & Team Introductions (Room 201)\n"
                        "09:30–10:30  Project Overview & Objectives (Room 201)\n"
                        "10:30–10:45  Break\n"
                        "10:45–12:00  Departmental Presentations (Room 202/203)\n"
                        "12:00–13:00  Lunch (Cafeteria)\n"
                        "13:00–14:00  Risk Management Workshop (Room 204)\n"
                        "14:00–14:15  Break\n"
                        "14:15–15:30  Team Discussion & Q&A (Room 204)\n"
                        "15:30–16:00  Action Items & Next Steps (Room 204)\n"
                        "16:00–16:30  Facility Tour (Start: Lobby)\n"
                        "Note: Remote participants join via video link for all sessions except Facility Tour."
                    ),
                    "translation": (
                        "프로젝트 피닉스 킥오프 – 상세 일정표\n\n"
                        "08:40–09:00  등록 및 커피 (로비)\n"
                        "09:00–09:30  환영 및 팀 소개 (201호)\n"
                        "09:30–10:30  프로젝트 개요 및 목표 (201호)\n"
                        "10:30–10:45  휴식\n"
                        "10:45–12:00  부서별 발표 (202/203호)\n"
                        "12:00–13:00  점심 (구내식당)\n"
                        "13:00–14:00  리스크 관리 워크숍 (204호)\n"
                        "14:00–14:15  휴식\n"
                        "14:15–15:30  팀 토의 및 질의응답 (204호)\n"
                        "15:30–16:00  실행 과제 및 차기 일정 (204호)\n"
                        "16:00–16:30  시설 투어 (출발: 로비)\n"
                        "참고: 원격 참석자는 시설 투어를 제외한 모든 세션에 화상 링크로 참여."
                    ),
                },
                {
                    "seq": 3,
                    "type": "Notice",
                    "text": (
                        "**Notice to All Project Phoenix Participants**\n\n"
                        "- Please arrive at least 15 minutes before the first session for registration and coffee in the lobby.\n"
                        "- Room 201 is on the second floor next to the elevator; Rooms 202/203/204 are in the same corridor.\n"
                        "- Lunch will be provided in the cafeteria. Vegetarian and gluten-free options are available upon request (notify by May 30).\n"
                        "- Bring your employee ID for building access. Wi-Fi information will be provided at registration.\n"
                        "- For remote participants: Test your video/audio setup in advance. Technical support is available from 08:30.\n"
                        "- For questions or special assistance, contact the admin office at ext. 123 or email admin@phoenix.com."
                    ),
                    "translation": (
                        "**프로젝트 피닉스 참가자 안내**\n\n"
                        "- 첫 세션 시작 15분 전까지 로비에서 등록 및 커피를 마치고 입장해 주세요.\n"
                        "- 201호는 2층 엘리베이터 옆, 202/203/204호는 같은 복도에 위치합니다.\n"
                        "- 점심은 구내식당에서 제공되며, 채식·글루텐 프리 메뉴는 5월 30일까지 요청 시 제공됩니다.\n"
                        "- 건물 출입을 위해 사원증을 반드시 지참하세요. 와이파이 정보는 등록 시 안내됩니다.\n"
                        "- 원격 참석자는 사전 영상·음성 테스트를 권장하며, 기술 지원은 08:30부터 가능합니다.\n"
                        "- 문의나 특별 지원 요청은 내선 123 또는 admin@phoenix.com으로 연락 바랍니다."
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "Where will the Risk Management Workshop be held?",
                    "questionTranslation": "리스크 관리 워크숍은 어디에서 진행됩니까?",
                    "choices": [
                        {"id": "A", "text": "Room 201", "translation": "201호"},
                        {"id": "B", "text": "Room 202", "translation": "202호"},
                        {"id": "C", "text": "Room 204", "translation": "204호"},
                        {"id": "D", "text": "Cafeteria", "translation": "구내식당"},
                    ],
                    "answer": "C",
                    "explanation": "일정표에 13:00–14:00 리스크 관리 워크숍이 204호에서 진행된다고 명시됨.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What should participants bring for building access?",
                    "questionTranslation": "참가자는 건물 출입을 위해 무엇을 지참해야 합니까?",
                    "choices": [
                        {"id": "A", "text": "Employee ID", "translation": "사원증"},
                        {
                            "id": "B",
                            "text": "Lunch voucher",
                            "translation": "점심 식권",
                        },
                        {
                            "id": "C",
                            "text": "Printed schedule",
                            "translation": "인쇄된 일정표",
                        },
                        {
                            "id": "D",
                            "text": "Parking permit",
                            "translation": "주차 허가증",
                        },
                    ],
                    "answer": "A",
                    "explanation": "안내문에 사원증 지참 명시.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "정보연계",
                    "questionText": "If a participant is vegetarian but forgets to notify the team by May 30, what meal will likely be provided?",
                    "questionTranslation": "참가자가 채식주의자이나 5월 30일까지 미리 알리지 않은 경우 어떤 식사가 제공됩니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Standard meal",
                            "translation": "일반 식사",
                        },
                        {
                            "id": "B",
                            "text": "Vegetarian meal",
                            "translation": "채식 식사",
                        },
                        {"id": "C", "text": "No meal", "translation": "식사 제공 없음"},
                        {
                            "id": "D",
                            "text": "Gluten-free meal",
                            "translation": "글루텐 프리 식사",
                        },
                    ],
                    "answer": "A",
                    "explanation": "안내문에 요청 시에만 채식/글루텐 프리 제공, 미요청 시 일반 식사 제공.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "정보연계",
                    "questionText": (
                        "A remote participant wants to join the Team Discussion & Q&A session but is unsure about technical support. "
                        "Based on all three passages, what should they do and when is support available?"
                    ),
                    "questionTranslation": (
                        "원격 참석자가 팀 토의 및 질의응답 세션에 참여하려고 하나 기술 지원이 걱정됩니다. "
                        "세 지문을 종합할 때, 어떻게 해야 하며 기술 지원은 언제부터 가능한가요?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "Test video/audio in advance; support available from 08:30",
                            "translation": "사전 테스트, 08:30부터 지원 가능",
                        },
                        {
                            "id": "B",
                            "text": "Arrive at Room 204 by 13:00",
                            "translation": "13:00까지 204호 도착",
                        },
                        {
                            "id": "C",
                            "text": "Email the manager after the session",
                            "translation": "세션 후 매니저에게 이메일",
                        },
                        {
                            "id": "D",
                            "text": "No support is available",
                            "translation": "지원 불가",
                        },
                    ],
                    "answer": "A",
                    "explanation": "안내문에 원격 참석자는 사전 테스트 권장, 기술 지원 08:30부터 가능 명시.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "정보연계",
                    "questionText": (
                        "According to all three passages, what are two things every participant must do before the kickoff meeting?"
                    ),
                    "questionTranslation": (
                        "세 지문을 종합할 때, 모든 참가자가 킥오프 미팅 전에 반드시 해야 하는 두 가지는 무엇입니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "Prepare a self-introduction and bring onboarding forms",
                            "translation": "자기소개 준비, 온보딩 서류 지참",
                        },
                        {
                            "id": "B",
                            "text": "Submit lunch preferences and parking permit",
                            "translation": "점심 메뉴 및 주차 허가증 제출",
                        },
                        {
                            "id": "C",
                            "text": "Send a technical support request and print the schedule",
                            "translation": "기술 지원 요청, 일정표 인쇄",
                        },
                        {
                            "id": "D",
                            "text": "Arrive at the cafeteria by 12:00 and bring a guest",
                            "translation": "12시까지 구내식당 도착, 동반자 지참",
                        },
                    ],
                    "answer": "A",
                    "explanation": "이메일에 자기소개 준비, 온보딩 서류 지참 명시. 일정표와 안내문에도 모든 참가자 공통 준비사항임.",
                },
            ],
        }
    ]

    # 2) Chat + Article + Form
    chat_article_form = [
        {
            "part": 7,
            "difficulty": "Hard",
            "questionSetType": "Triple",
            "passages": [
                {
                    "seq": 1,
                    "type": "Chat",
                    "text": (
                        "[08:45] Mina: Did you read the article about the city marathon?\n"
                        "[08:46] Jisoo: Yes! I’m thinking of signing up, but I’m not sure which course to choose.\n"
                        "[08:47] Mina: I did the 5K last year. It was fun, but the 10K has a new route this time.\n"
                        "[08:48] Jisoo: I saw there’s a group discount if we register together. Want to join as a team?\n"
                        "[08:49] Mina: Sure! Let’s check the details and see if we can get the early bird T-shirt.\n"
                        "[08:50] Jisoo: I’ll fill out the form and send you my info. Registration closes soon, right?\n"
                        "[08:51] Mina: Yes, by Friday. Also, don’t forget to list your emergency contact and select your T-shirt size. See you at the finish line!"
                    ),
                    "translation": (
                        "[08:45] 미나: 시 마라톤 기사 읽어봤어?\n"
                        "[08:46] 지수: 응! 나 신청할까 고민 중인데, 코스를 뭘로 할지 모르겠어.\n"
                        "[08:47] 미나: 나 작년에 5km 뛰었는데 재밌었어. 이번엔 10km 코스가 새로 생겼대.\n"
                        "[08:48] 지수: 단체 등록하면 할인 있던데, 우리 팀으로 신청할래?\n"
                        "[08:49] 미나: 좋아! 세부사항 확인하고 얼리버드 티셔츠 받을 수 있는지도 보자.\n"
                        "[08:50] 지수: 내가 양식 작성해서 정보 보낼게. 등록 곧 마감이지?\n"
                        "[08:51] 미나: 응, 금요일까지야. 비상 연락처랑 티셔츠 사이즈도 꼭 선택해야 해. 결승선에서 보자!"
                    ),
                },
                {
                    "seq": 2,
                    "type": "Article",
                    "text": (
                        "City Marathon Returns with New Features\n\n"
                        "The annual City Marathon will take place on June 20, starting at Riverside Park and finishing at City Hall Plaza. "
                        "Participants can choose between a 5K and a 10K course, with the 10K route passing through the historic district for the first time. "
                        "Registration is open until May 22 (Friday), and group discounts are available for teams of four or more. "
                        "Early registrants (by May 15) will receive a limited-edition T-shirt in addition to the standard race shirt and a finisher’s medal. "
                        "All runners must provide an emergency contact and select their preferred T-shirt size on the registration form. "
                        "Water stations and first-aid tents will be set up along both routes. For more information, visit www.citymarathon.com or call (555) 123-9876."
                    ),
                    "translation": (
                        "시 마라톤, 새로운 코스와 함께 돌아온다\n\n"
                        "연례 시 마라톤이 6월 20일 리버사이드 공원에서 출발해 시청 광장에서 마무리됩니다. "
                        "참가자는 5km 또는 10km 코스를 선택할 수 있으며, 10km 코스는 올해 처음으로 역사 지구를 통과합니다. "
                        "등록은 5월 22일(금)까지이며, 4인 이상 단체 등록 시 할인 혜택이 있습니다. "
                        "5월 15일까지 등록한 참가자에게는 한정판 티셔츠가 추가로 제공되며, 모든 참가자는 기본 티셔츠와 완주 메달을 받습니다. "
                        "모든 주자는 신청서에 비상 연락처와 티셔츠 사이즈를 반드시 기재해야 합니다. "
                        "양 코스에는 급수대와 응급 처치소가 설치됩니다. 자세한 내용은 www.citymarathon.com 또는 (555) 123-9876으로 문의하세요."
                    ),
                },
                {
                    "seq": 3,
                    "type": "Form",
                    "text": (
                        "City Marathon Registration Form (Sample)\n\n"
                        "Name: Jisoo Kim\n"
                        "Distance: [ ] 5K   [X] 10K\n"
                        "T-shirt Size: [ ] S [X] M [ ] L [ ] XL\n"
                        "Emergency Contact: Mina Park (010-1234-5678)\n"
                        "Team Name (if any): Morning Runners\n"
                        "Registration Date: May 14\n"
                        "Payment Method: Credit Card\n"
                        "Signature: Jisoo Kim"
                    ),
                    "translation": (
                        "시 마라톤 참가 신청서 (예시)\n\n"
                        "이름: 김지수\n"
                        "거리: [ ] 5km   [X] 10km\n"
                        "티셔츠 사이즈: [ ] S [X] M [ ] L [ ] XL\n"
                        "비상 연락처: 박미나 (010-1234-5678)\n"
                        "팀명(해당 시): Morning Runners\n"
                        "등록일: 5월 14일\n"
                        "결제 방법: 신용카드\n"
                        "서명: 김지수"
                    ),
                },
            ],
            "questions": [
                {
                    "questionSeq": 1,
                    "questionType": "세부사항",
                    "questionText": "What is the registration deadline for the marathon?",
                    "questionTranslation": "마라톤 등록 마감일은 언제입니까?",
                    "choices": [
                        {"id": "A", "text": "May 15", "translation": "5월 15일"},
                        {"id": "B", "text": "May 22", "translation": "5월 22일"},
                        {"id": "C", "text": "June 20", "translation": "6월 20일"},
                        {"id": "D", "text": "June 15", "translation": "6월 15일"},
                    ],
                    "answer": "B",
                    "explanation": "기사에 5월 22일까지 등록 가능하다고 명시됨.",
                },
                {
                    "questionSeq": 2,
                    "questionType": "세부사항",
                    "questionText": "What special benefit does Jisoo receive by registering on May 14?",
                    "questionTranslation": "지수가 5월 14일에 등록함으로써 받는 특별 혜택은 무엇입니까?",
                    "choices": [
                        {
                            "id": "A",
                            "text": "A group discount only",
                            "translation": "단체 할인만",
                        },
                        {
                            "id": "B",
                            "text": "A limited-edition T-shirt",
                            "translation": "한정판 티셔츠",
                        },
                        {
                            "id": "C",
                            "text": "A free meal voucher",
                            "translation": "무료 식사 쿠폰",
                        },
                        {"id": "D", "text": "A water bottle", "translation": "물병"},
                    ],
                    "answer": "B",
                    "explanation": "5월 15일 이전 등록자는 한정판 티셔츠를 받음.",
                },
                {
                    "questionSeq": 3,
                    "questionType": "정보연계",
                    "questionText": (
                        "Based on the chat, article, and form, which of the following is true about Jisoo’s registration?"
                    ),
                    "questionTranslation": (
                        "채팅, 기사, 신청서를 종합할 때 지수의 등록에 대해 옳은 것은 무엇입니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "She registered as part of a team and chose the 10K course.",
                            "translation": "팀으로 등록했고 10km 코스를 선택했다",
                        },
                        {
                            "id": "B",
                            "text": "She registered individually for the 5K course.",
                            "translation": "개인으로 5km 코스에 등록했다",
                        },
                        {
                            "id": "C",
                            "text": "She did not provide an emergency contact.",
                            "translation": "비상 연락처를 기재하지 않았다",
                        },
                        {
                            "id": "D",
                            "text": "She missed the early registration deadline.",
                            "translation": "얼리버드 마감일을 놓쳤다",
                        },
                    ],
                    "answer": "A",
                    "explanation": "신청서에 팀명, 10km 선택, 비상 연락처 모두 기재됨.",
                },
                {
                    "questionSeq": 4,
                    "questionType": "정보연계",
                    "questionText": (
                        "If Mina wants to receive the limited-edition T-shirt but registers on May 16, will she get it? Use all three passages to support your answer."
                    ),
                    "questionTranslation": (
                        "미나가 5월 16일에 등록하면 한정판 티셔츠를 받을 수 있습니까? 세 지문을 근거로 답하세요."
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "No, because the early registration deadline is May 15.",
                            "translation": "아니오, 얼리버드 마감이 5월 15일이기 때문",
                        },
                        {
                            "id": "B",
                            "text": "Yes, because registration is open until May 22.",
                            "translation": "예, 5월 22일까지 등록 가능하므로",
                        },
                        {
                            "id": "C",
                            "text": "Yes, if she joins a team.",
                            "translation": "예, 팀으로 등록하면 가능",
                        },
                        {
                            "id": "D",
                            "text": "Only if she chooses the 5K course.",
                            "translation": "5km 코스 선택 시만 가능",
                        },
                    ],
                    "answer": "A",
                    "explanation": "기사에 5월 15일까지 등록해야 한정판 티셔츠 제공 명시.",
                },
                {
                    "questionSeq": 5,
                    "questionType": "정보연계",
                    "questionText": (
                        "According to the article and the sample form, what information is mandatory for all marathon registrants?"
                    ),
                    "questionTranslation": (
                        "기사와 신청서 예시를 근거로, 모든 마라톤 참가자가 반드시 기재해야 하는 정보는 무엇입니까?"
                    ),
                    "choices": [
                        {
                            "id": "A",
                            "text": "Emergency contact and T-shirt size",
                            "translation": "비상 연락처와 티셔츠 사이즈",
                        },
                        {
                            "id": "B",
                            "text": "Previous race time and payment method",
                            "translation": "이전 기록과 결제 방법",
                        },
                        {
                            "id": "C",
                            "text": "Team name and meal preference",
                            "translation": "팀명과 식사 선호",
                        },
                        {
                            "id": "D",
                            "text": "Passport number and address",
                            "translation": "여권 번호와 주소",
                        },
                    ],
                    "answer": "A",
                    "explanation": "기사와 신청서 모두 비상 연락처, 티셔츠 사이즈 필수 기재 명시.",
                },
            ],
        }
    ]
