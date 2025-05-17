class Part6FewShotExamples:
    """
    TOEIC Part 6 few-shot examples for each passageType.
    """

    # 1) Email / Letter
    email_letter = [
        {
            "part": 6,
            "passageType": "Email/Letter",
            "difficulty": "Medium",
            "passage": (
                "Subject: Team Building Workshop\n\n"
                "(A) Dear Marketing Team,\n"
                "We are excited to announce that a one-day workshop has been ___1___ "
                "for Friday, July 12. (B) The program will focus on strengthening "
                "communication skills; ___2___, it will include outdoor activities to "
                "encourage collaboration. ___3___ (C) Please review the attached agenda and "
                "confirm your attendance by June 30. (D)\n\n"
                "Best regards,\nHR Department"
            ),
            "passageTranslation": (
                "제목: 팀 빌딩 워크숍 안내\n\n"
                "(A) 마케팅팀 여러분께,\n"
                "7월 12일(금) 하루 일정으로 팀 빌딩 워크숍이 ___1___ 예정되어 있습니다. "
                "(B) 이번 프로그램은 의사소통 역량 강화에 초점을 두며, ___2___ 야외 활동을 통해 "
                "협업을 장려할 예정입니다. ___3___ (C) 첨부된 일정을 확인하시고 6월 30일까지 참석 여부를 "
                "회신해 주시기 바랍니다. (D)\n\n"
                "인사팀 드림"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "arranged", "translation": "준비된"},
                        {"id": "B", "text": "arrange", "translation": "준비하다"},
                        {"id": "C", "text": "arranging", "translation": "준비 중인"},
                        {"id": "D", "text": "arrangement", "translation": "준비"},
                    ],
                    "answer": "A",
                    "explanation": "'has been arranged' 현재완료 수동태 사용.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {
                            "id": "A",
                            "text": "otherwise",
                            "translation": "그렇지 않으면",
                        },
                        {"id": "B", "text": "for example", "translation": "예를 들어"},
                        {"id": "C", "text": "in addition", "translation": "추가로"},
                        {
                            "id": "D",
                            "text": "nevertheless",
                            "translation": "그럼에도 불구하고",
                        },
                    ],
                    "answer": "C",
                    "explanation": "앞뒤 문장을 덧붙이는 추가 정보이므로 'in addition' 적합.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Lunch will be provided at no cost to participants.",
                            "translation": "참가자에게 무료 점심이 제공됩니다.",
                        },
                        {
                            "id": "B",
                            "text": "The venue has limited parking spaces.",
                            "translation": "장소 주차 공간이 제한적입니다.",
                        },
                        {
                            "id": "C",
                            "text": "Please wear formal business attire.",
                            "translation": "정장을 착용해 주십시오.",
                        },
                        {
                            "id": "D",
                            "text": "Workshop feedback forms will follow.",
                            "translation": "워크숍 피드백 양식이 추후 제공됩니다.",
                        },
                    ],
                    "answer": "A",
                    "explanation": "행사 안내 흐름상 '점심 제공' 문장이 자연스럽게 이어집니다.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "C",
                    "explanation": "행정적 요청(회신 확인)은 본문 끝부분인 (C)에 두는 것이 자연스러움.",
                },
            ],
        }
    ]

    # 2) Memo
    memo = [
        {
            "part": 6,
            "passageType": "Memo",
            "difficulty": "Easy",
            "passage": (
                "MEMORANDUM\n\n"
                "To: All Staff\nFrom: IT Manager\nDate: March 3\nSubject: Printer Downtime\n\n"
                "(A) Please be advised that the main office printer will be ___1___ "
                "for maintenance on March 5 from 1 p.m. to 3 p.m. (B) ___2___ you have "
                "urgent printing needs, contact the reception desk to access the backup "
                "device. ___3___ (C) We apologize for any inconvenience this may cause. (D)\n"
            ),
            "passageTranslation": (
                "메모\n\n"
                "수신: 전 직원\n발신: IT 매니저\n일자: 3월 3일\n제목: 프린터 점검 공지\n\n"
                "(A) 본사 프린터가 3월 5일 13:00-15:00 동안 ___1___ 점검될 예정입니다. "
                "(B) ___2___ 긴급 인쇄가 필요하신 경우 리셉션에서 예비 프린터를 이용해 주십시오. "
                "___3___ (C) 불편을 끼쳐 드려 죄송합니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "out", "translation": "밖에"},
                        {
                            "id": "B",
                            "text": "offline",
                            "translation": "오프라인 상태인",
                        },
                        {"id": "C", "text": "off", "translation": "꺼진"},
                        {"id": "D", "text": "up", "translation": "위에"},
                    ],
                    "answer": "B",
                    "explanation": "'be offline' 유지보수 의미.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {"id": "A", "text": "If", "translation": "만약"},
                        {"id": "B", "text": "Unless", "translation": "~하지 않는 한"},
                        {"id": "C", "text": "So", "translation": "그래서"},
                        {"id": "D", "text": "Because", "translation": "~때문에"},
                    ],
                    "answer": "A",
                    "explanation": "조건문 도입: 'If you have urgent needs'.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "All queued jobs will resume automatically afterward.",
                            "translation": "대기 중인 인쇄 작업은 이후 자동 재개됩니다.",
                        },
                        {
                            "id": "B",
                            "text": "Paper jams have been frequent recently.",
                            "translation": "최근 용지 걸림이 자주 발생했습니다.",
                        },
                        {
                            "id": "C",
                            "text": "Replacement toner is on order.",
                            "translation": "토너 교체품이 주문되었습니다.",
                        },
                        {
                            "id": "D",
                            "text": "We will post an update if the schedule changes.",
                            "translation": "일정이 변경되면 업데이트를 공지하겠습니다.",
                        },
                    ],
                    "answer": "D",
                    "explanation": "공사 일정 변동 안내가 사과문(불편) 흐름과 연결.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "B",
                    "explanation": "'backup device 안내' 후 (B) 이후 삽입 위치가 자연스러움.",
                },
            ],
        }
    ]
    # 3) Advertisement
    advertisement = [
        {
            "part": 6,
            "passageType": "Advertisement",
            "difficulty": "Medium",
            "passage": (
                "Grand Opening — Riverside Fitness Center\n\n"
                "(A) Join us this Saturday for the ___1___ of our state-of-the-art gym. "
                "(B) The first 100 visitors will receive a free merchandise bundle; "
                "___2___, members who sign up before May 31 will enjoy a 20 % discount on the annual plan. "
                "___3___ (C) Bring this flyer to the reception desk to claim your gift. (D)\n"
            ),
            "passageTranslation": (
                "그랜드 오픈 — 리버사이드 피트니스 센터\n\n"
                "(A) 최신 시설을 갖춘 체육관의 ___1___ 행사에 이번 토요일 함께하세요. "
                "(B) 선착순 100명에게 무료 기념품 세트를 드리며, ___2___ 5월 31일까지 가입하시면 "
                "연간 회원권을 20 % 할인해 드립니다. ___3___ (C) 이 전단지를 데스크에 제시하면 "
                "사은품을 받을 수 있습니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "celebration", "translation": "축하 행사"},
                        {"id": "B", "text": "celebrate", "translation": "축하하다"},
                        {"id": "C", "text": "celebrating", "translation": "축하하는"},
                        {"id": "D", "text": "celebratory", "translation": "축하의"},
                    ],
                    "answer": "A",
                    "explanation": "‘for the celebration of’ 명사 형태 적합.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {
                            "id": "A",
                            "text": "otherwise",
                            "translation": "그렇지 않으면",
                        },
                        {"id": "B", "text": "additionally", "translation": "추가로"},
                        {"id": "C", "text": "meanwhile", "translation": "그러는 동안"},
                        {"id": "D", "text": "therefore", "translation": "그러므로"},
                    ],
                    "answer": "B",
                    "explanation": "선물 안내에 혜택 정보를 덧붙여 제시 → ‘additionally’.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Tours of the facility will run every hour on the hour.",
                            "translation": "시설 투어가 매 정시에 진행됩니다.",
                        },
                        {
                            "id": "B",
                            "text": "Parking spaces are limited after 6 p.m.",
                            "translation": "오후 6시 이후 주차 공간이 제한됩니다.",
                        },
                        {
                            "id": "C",
                            "text": "Child-care services are unavailable.",
                            "translation": "어린이 돌봄 서비스는 제공되지 않습니다.",
                        },
                        {
                            "id": "D",
                            "text": "Please follow us on social media for updates.",
                            "translation": "업데이트는 SNS에서 확인해 주세요.",
                        },
                    ],
                    "answer": "A",
                    "explanation": "행사 안내(투어) 문장이 홍보 내용 흐름과 자연스럽게 연결.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "C",
                    "explanation": "교환 절차 안내는 쿠폰 제시 문장(C)에 두는 것이 자연스러움.",
                },
            ],
        }
    ]

    # 4) Notice
    notice = [
        {
            "part": 6,
            "passageType": "Notice",
            "difficulty": "Easy",
            "passage": (
                "Notice: Elevator Inspection\n\n"
                "(A) All tenants are informed that the building’s main elevator will be ___1___ "
                "on Tuesday, September 14, from 10:00 a.m. to 2:00 p.m. "
                "(B) ___2___, please use the service elevator located near the loading dock. "
                "___3___ (C) We apologize for the inconvenience and appreciate your cooperation. (D)\n"
            ),
            "passageTranslation": (
                "공지: 엘리베이터 점검\n\n"
                "(A) 본관 주 엘리베이터가 9월 14일 화요일 10:00-14:00 동안 ___1___ 예정입니다. "
                "(B) ___2___ 하시는 경우, 하역장 근처의 서비스 엘리베이터를 이용해 주십시오. "
                "___3___ (C) 불편을 드려 죄송하며 협조에 감사드립니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "inspecting", "translation": "점검하는 중"},
                        {"id": "B", "text": "inspected", "translation": "점검될"},
                        {"id": "C", "text": "inspection", "translation": "점검"},
                        {"id": "D", "text": "inspect", "translation": "점검하다"},
                    ],
                    "answer": "B",
                    "explanation": "‘will be inspected’ 수동태 필요한 자리.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {"id": "A", "text": "If possible", "translation": "가능하다면"},
                        {"id": "B", "text": "For instance", "translation": "예를 들어"},
                        {"id": "C", "text": "In the meantime", "translation": "그동안"},
                        {"id": "D", "text": "As a result", "translation": "그 결과"},
                    ],
                    "answer": "C",
                    "explanation": "점검 ‘동안’ 대체 수단 안내 → ‘In the meantime’.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "The stairwells will remain accessible at all times.",
                            "translation": "계단은 항상 이용 가능합니다.",
                        },
                        {
                            "id": "B",
                            "text": "Smoking is prohibited inside the building.",
                            "translation": "건물 내 흡연 금지입니다.",
                        },
                        {
                            "id": "C",
                            "text": "Pets must be kept on a leash in common areas.",
                            "translation": "공용 구역에서 반려동물은 목줄 필수입니다.",
                        },
                        {
                            "id": "D",
                            "text": "Fire drills are conducted quarterly.",
                            "translation": "화재 대피 훈련은 분기마다 실시됩니다.",
                        },
                    ],
                    "answer": "A",
                    "explanation": "엘리베이터 대안 안내 흐름 강화.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "B",
                    "explanation": "계단 이용 안내는 대체 이동 수단 안내문(B)가 가장 자연스럽다.",
                },
            ],
        }
    ]

    # 5) Article
    article = [
        {
            "part": 6,
            "passageType": "Article",
            "difficulty": "Medium",
            "passage": (
                "City Gazette — Technology Section\n\n"
                "(A) According to a recent survey, more than 60 % of commuters now use "
                "mobile apps to track bus arrival times. ___1___ "
                "(B) The city’s transit authority launched its official real-time tracker "
                "last year; ___2___, private developers have introduced additional features "
                "such as crowd-level predictions. ___3___ (C) Experts predict that these tools "
                "will reduce wait times at major stops by 15 %. (D)\n"
            ),
            "passageTranslation": (
                "시티 가제트 — 기술 섹션\n\n"
                "(A) 최근 조사에 따르면 통근자의 60 % 이상이 버스 도착 시간을 확인하기 위해 "
                "모바일 앱을 사용하고 있습니다. ___1___ "
                "(B) 시 교통공사는 지난해 공식 실시간 추적기를 출시했으며, ___2___ "
                "민간 개발자들은 혼잡도 예측과 같은 추가 기능을 내놓았습니다. "
                "___3___ (C) 전문가들은 이러한 도구가 주요 정류장의 대기 시간을 15 % 줄일 것으로 전망합니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {
                            "id": "A",
                            "text": "As a consequence",
                            "translation": "그 결과",
                        },
                        {
                            "id": "B",
                            "text": "Nevertheless",
                            "translation": "그럼에도 불구하고",
                        },
                        {"id": "C", "text": "In contrast", "translation": "대조적으로"},
                        {"id": "D", "text": "For instance", "translation": "예를 들어"},
                    ],
                    "answer": "D",
                    "explanation": "'예를 들어' 뒤에 구체 사례가 나올 문맥.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {"id": "A", "text": "meanwhile", "translation": "한편"},
                        {"id": "B", "text": "therefore", "translation": "그러므로"},
                        {
                            "id": "C",
                            "text": "otherwise",
                            "translation": "그렇지 않으면",
                        },
                        {"id": "D", "text": "besides", "translation": "게다가"},
                    ],
                    "answer": "A",
                    "explanation": "공공 앱 출시 후 ‘한편’ 민간 앱 이야기를 잇는 흐름.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Some riders still prefer printed timetables.",
                            "translation": "일부 승객은 여전히 인쇄된 시간표를 선호합니다.",
                        },
                        {
                            "id": "B",
                            "text": "The study included more than 10,000 respondents.",
                            "translation": "해당 조사는 1만 명 이상이 참여했습니다.",
                        },
                        {
                            "id": "C",
                            "text": "Similar technologies are being tested in neighboring cities.",
                            "translation": "인근 도시에서도 유사 기술이 시험 중입니다.",
                        },
                        {
                            "id": "D",
                            "text": "Ticket prices have remained unchanged for three years.",
                            "translation": "요금은 3년간 동결되었습니다.",
                        },
                    ],
                    "answer": "C",
                    "explanation": "‘Expert predict…’ 국제 동향 확장 설명으로 자연스럽다.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "C",
                    "explanation": "국제 사례 문장(C)에 배치해 ‘예측’ 문단을 보강.",
                },
            ],
        }
    ]

    # 6) Instruction
    instruction = [
        {
            "part": 6,
            "passageType": "Instruction",
            "difficulty": "Easy",
            "passage": (
                "Installing the XF-200 Router\n\n"
                "(A) Before starting, ensure that your modem is powered off. "
                "Connect the modem to the router’s WAN port using the supplied cable. "
                "___1___ (B) Next, plug the router into an electrical outlet; ___2___, "
                "turn the modem back on. ___3___ (C) Wait until the indicator light turns solid green. (D)\n"
            ),
            "passageTranslation": (
                "XF-200 라우터 설치 방법\n\n"
                "(A) 시작 전에 모뎀 전원을 끕니다. "
                "제공된 케이블로 모뎀을 라우터 WAN 포트에 연결합니다. ___1___ "
                "(B) 다음으로 라우터 전원을 연결한 후 ___2___ 모뎀 전원을 다시 켭니다. "
                "___3___ (C) 표시등이 녹색으로 고정될 때까지 기다립니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "Afterward", "translation": "그 후에"},
                        {"id": "B", "text": "Meanwhile", "translation": "그동안"},
                        {"id": "C", "text": "During", "translation": "~동안"},
                        {"id": "D", "text": "Unless", "translation": "~하지 않는 한"},
                    ],
                    "answer": "A",
                    "explanation": "작업 순서를 나타내는 부사.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {"id": "A", "text": "in other words", "translation": "즉"},
                        {
                            "id": "B",
                            "text": "for that reason",
                            "translation": "그 이유로",
                        },
                        {"id": "C", "text": "after that", "translation": "그 후에"},
                        {
                            "id": "D",
                            "text": "at the same time",
                            "translation": "동시에",
                        },
                    ],
                    "answer": "C",
                    "explanation": "전원 연결 ‘후’ 순서 연결.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "This process may take up to two minutes.",
                            "translation": "이 과정은 최대 2분 정도 걸릴 수 있습니다.",
                        },
                        {
                            "id": "B",
                            "text": "Avoid placing the router near large metal objects.",
                            "translation": "라우터를 큰 금속 물체 근처에 두지 마십시오.",
                        },
                        {
                            "id": "C",
                            "text": "Contact your ISP if the light stays red.",
                            "translation": "빨간 불이 지속되면 ISP에 문의하십시오.",
                        },
                        {
                            "id": "D",
                            "text": "Resetting the device will erase custom settings.",
                            "translation": "장치를 초기화하면 사용자 설정이 삭제됩니다.",
                        },
                    ],
                    "answer": "A",
                    "explanation": "지연 시간 안내가 기다림 단계(C)와 자연스럽게 이어짐.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "C",
                    "explanation": "‘최대 2분 소요’ 문장은 대기 안내(C)가 가장 자연스럽다.",
                },
            ],
        }
    ]

    # 7) Form
    form = [
        {
            "part": 6,
            "passageType": "Form",
            "difficulty": "Medium",
            "passage": (
                "Conference Registration Form (excerpt)\n\n"
                "(A) Participant Name: __________________\n"
                "Company: __________________\n\n"
                "Please select your preferred breakout session. ___1___ "
                "(B) If you choose Session B, ___2___ select a lunch option. "
                "___3___ (C) Payment must be received by June 10 to confirm your spot. (D)\n"
            ),
            "passageTranslation": (
                "컨퍼런스 등록 양식 (발췌)\n\n"
                "(A) 참가자 이름: __________________\n"
                "소속 회사: __________________\n\n"
                "희망 분과 세션을 선택해 주세요. ___1___ "
                "(B) 세션 B를 선택하시는 경우, ___2___ 점심 옵션을 선택해야 합니다. "
                "___3___ (C) 좌석 확정을 위해 6월 10일까지 결제가 완료되어야 합니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "Note", "translation": "유의하세요"},
                        {"id": "B", "text": "Noting", "translation": "유의하는 중"},
                        {"id": "C", "text": "Noted", "translation": "유의한"},
                        {"id": "D", "text": "Notes", "translation": "노트"},
                    ],
                    "answer": "A",
                    "explanation": "지시문 시작 → 명령형 ‘Note’ 적절.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {"id": "A", "text": "overwise", "translation": "잘못된 철자"},
                        {"id": "B", "text": "please", "translation": "부탁드립니다"},
                        {"id": "C", "text": "likewise", "translation": "마찬가지로"},
                        {
                            "id": "D",
                            "text": "otherwise",
                            "translation": "그렇지 않으면",
                        },
                    ],
                    "answer": "D",
                    "explanation": "선택 조건 미이행 시 결과 → ‘otherwise’.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Session C is already fully booked.",
                            "translation": "세션 C는 이미 마감되었습니다.",
                        },
                        {
                            "id": "B",
                            "text": "Early-bird pricing ends on May 15.",
                            "translation": "얼리버드 가격은 5월 15일 종료됩니다.",
                        },
                        {
                            "id": "C",
                            "text": "Cancellations received after June 1 are non-refundable.",
                            "translation": "6월 1일 이후 취소는 환불되지 않습니다.",
                        },
                        {
                            "id": "D",
                            "text": "Name badges will be distributed at the entrance.",
                            "translation": "명찰은 입구에서 배부됩니다.",
                        },
                    ],
                    "answer": "B",
                    "explanation": "결제 안내(D)에 앞서 비용 관련 정보를 제공하면 자연스럽다.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "C",
                    "explanation": "가격 안내 문장은 결제 기한(C) 바로 앞(B 뒤)에 두는 편이 적절.",
                },
            ],
        }
    ]

    # 8) Schedule
    schedule = [
        {
            "part": 6,
            "passageType": "Schedule",
            "difficulty": "Easy",
            "passage": (
                "Shuttle Bus Schedule — Airport ↔ Downtown\n\n"
                "(A) Buses depart every 30 minutes from 5 a.m. to 11 p.m. ___1___ "
                "(B) Travel time is approximately 45 minutes; ___2___, "
                "traffic conditions may cause delays during peak hours. "
                "___3___ (C) Tickets can be purchased online or from the driver. (D)\n"
            ),
            "passageTranslation": (
                "셔틀버스 운행표 — 공항 ↔ 다운타운\n\n"
                "(A) 05:00-23:00 동안 30분 간격으로 출발합니다. ___1___ "
                "(B) 소요 시간은 약 45분이며 ___2___ 러시아워에는 교통 상황으로 인해 지연될 수 있습니다. "
                "___3___ (C) 티켓은 온라인 또는 운전기사에게서 구매 가능합니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Nevertheless",
                            "translation": "그럼에도 불구하고",
                        },
                        {"id": "B", "text": "Please note", "translation": "유의하세요"},
                        {"id": "C", "text": "However", "translation": "그러나"},
                        {"id": "D", "text": "Because", "translation": "~때문에"},
                    ],
                    "answer": "B",
                    "explanation": "안내문 강조 → ‘Please note’.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {
                            "id": "A",
                            "text": "otherwise",
                            "translation": "그렇지 않으면",
                        },
                        {"id": "B", "text": "for example", "translation": "예를 들어"},
                        {"id": "C", "text": "in addition", "translation": "추가로"},
                        {"id": "D", "text": "however", "translation": "그러나"},
                    ],
                    "answer": "D",
                    "explanation": "표준 소요 시간 ↔ 지연 가능성 대비 → ‘그러나’.",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Each bus is equipped with free Wi-Fi.",
                            "translation": "각 버스에는 무료 와이파이가 제공됩니다.",
                        },
                        {
                            "id": "B",
                            "text": "Pets are not permitted on board.",
                            "translation": "애완동물 탑승 불가입니다.",
                        },
                        {
                            "id": "C",
                            "text": "Additional late-night trips run on Fridays.",
                            "translation": "금요일에는 심야 추가 운행이 있습니다.",
                        },
                        {
                            "id": "D",
                            "text": "Passengers must keep their tickets for inspection.",
                            "translation": "승객은 검사를 위해 티켓을 보관해야 합니다.",
                        },
                    ],
                    "answer": "C",
                    "explanation": "스케줄 안내와 자연스럽게 연결되는 ‘추가 운행’ 정보.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "A",
                    "explanation": "추가 운행 정보는 기본 운행표 설명(A) 바로 뒤가 적절.",
                },
            ],
        }
    ]

    # 9) Newsletter
    newsletter = [
        {
            "part": 6,
            "passageType": "Newsletter",
            "difficulty": "Medium",
            "passage": (
                "GreenTech Quarterly — Spring Edition\n\n"
                "(A) In this issue, we highlight three startups ___1___ are revolutionizing "
                "battery recycling. (B) ___2___ joining the clean-energy sector in record numbers, "
                "venture funding has surged by 25 % this year. ___3___ "
                "(C) Subscribers can register for our upcoming webinar on May 20. (D)\n"
            ),
            "passageTranslation": (
                "그린테크 분기 뉴스레터 — 봄호\n\n"
                "(A) 이번 호에서는 배터리 재활용 혁신을 이끄는 세 개 스타트업을 ___1___ 소개합니다. "
                "(B) ___2___ 클린에너지 분야에 rekord 수준으로 합류하면서, 벤처 투자가 올해 25 % 급증했습니다. "
                "___3___ (C) 구독자는 5월 20일 예정된 웨비나에 등록할 수 있습니다. (D)\n"
            ),
            "questions": [
                {
                    "blankNumber": 1,
                    "questionType": "어휘/문법",
                    "choices": [
                        {"id": "A", "text": "whom", "translation": "누구를"},
                        {"id": "B", "text": "which", "translation": "어떤"},
                        {"id": "C", "text": "that", "translation": "...하는"},
                        {"id": "D", "text": "whose", "translation": "~의"},
                    ],
                    "answer": "C",
                    "explanation": "선행사 ‘startups’를 받는 주격 관계대명사 ‘that’.",
                },
                {
                    "blankNumber": 2,
                    "questionType": "연결어",
                    "choices": [
                        {
                            "id": "A",
                            "text": "With entrepreneurs",
                            "translation": "기업가들이 ~함에 따라",
                        },
                        {"id": "B", "text": "In case", "translation": "만약 ~인 경우"},
                        {"id": "C", "text": "By contrast", "translation": "대조적으로"},
                        {"id": "D", "text": "Above all", "translation": "무엇보다도"},
                    ],
                    "answer": "A",
                    "explanation": "원인/결과 관계: ‘기업가들이 많이 참여함에 따라 자금 증가’. ",
                },
                {
                    "blankNumber": 3,
                    "questionType": "문장 삽입",
                    "choices": [
                        {
                            "id": "A",
                            "text": "Early registration guarantees a digital swag pack.",
                            "translation": "사전 등록 시 디지털 기념품을 제공합니다.",
                        },
                        {
                            "id": "B",
                            "text": "Printed copies will be discontinued next year.",
                            "translation": "내년부터 인쇄본 발행이 중단됩니다.",
                        },
                        {
                            "id": "C",
                            "text": "We also feature an interview with the Energy Minister.",
                            "translation": "또한 에너지 장관 인터뷰를 실었습니다.",
                        },
                        {
                            "id": "D",
                            "text": "Editorial feedback is welcome at any time.",
                            "translation": "편집 피드백은 언제든 환영합니다.",
                        },
                    ],
                    "answer": "C",
                    "explanation": "콘텐츠 소개(A)와 이어져 자연스럽다.",
                },
                {
                    "blankNumber": 4,
                    "questionType": "문장 위치",
                    "choices": [
                        {"id": "A", "text": "(A)", "translation": "(A)"},
                        {"id": "B", "text": "(B)", "translation": "(B)"},
                        {"id": "C", "text": "(C)", "translation": "(C)"},
                        {"id": "D", "text": "(D)", "translation": "(D)"},
                    ],
                    "answer": "B",
                    "explanation": "인터뷰 소개는 투자 현황(B)에 놓여도 콘텐츠 흐름이 자연스러움.",
                },
            ],
        }
    ]
