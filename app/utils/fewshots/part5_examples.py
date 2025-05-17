class Part5FewShotExamples:
    """
    This class contains examples for Part 5 of the project.
    """

    # 문법 - 시제
    grammar_tense = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "시제",
            "difficulty": "Medium",
            "questionText": "The sales figures ___ significantly since last quarter.",
            "questionTranslation": "지난 분기 이후 매출 수치가 크게 ___.",
            "choices": [
                {"id": "A", "text": "rise", "translation": "오른다"},
                {"id": "B", "text": "rose", "translation": "올랐다"},
                {"id": "C", "text": "have risen", "translation": "올랐다"},
                {"id": "D", "text": "rising", "translation": "오르는 중이다"},
            ],
            "answer": "C",
            "explanation": "과거 시점 시작→현재까지 결과 = 현재완료 ‘have risen’.",
            "vocabulary": [
                {
                    "word": "figure",
                    "meaning": "수치",
                    "partOfSpeech": "noun",
                    "example": "The sales figures increased last year.",
                    "exampleTranslation": "지난해 매출 수치가 증가했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "시제",
            "difficulty": "Medium",
            "questionText": "Mr. Sato will present the proposal after the team ___ it.",
            "questionTranslation": "팀이 제안서를 ___ 후 사토 씨가 발표할 것이다.",
            "choices": [
                {"id": "A", "text": "reviews", "translation": "검토한다"},
                {"id": "B", "text": "reviewed", "translation": "검토했다"},
                {
                    "id": "C",
                    "text": "has reviewed",
                    "translation": "검토해 왔다",
                },
                {
                    "id": "D",
                    "text": "will review",
                    "translation": "검토할 것이다",
                },
            ],
            "answer": "A",
            "explanation": "시간부사절(현재시제) → ‘after the team reviews’.",
            "vocabulary": [
                {
                    "word": "proposal",
                    "meaning": "제안서",
                    "partOfSpeech": "noun",
                    "example": "She submitted a proposal for the new project.",
                    "exampleTranslation": "그녀는 새 프로젝트에 대한 제안서를 제출했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "시제",
            "difficulty": "Medium",
            "questionText": "By the time you arrive, the conference ___.",
            "questionTranslation": "당신이 도착할 때쯤이면 회의가 ___ 것이다.",
            "choices": [
                {
                    "id": "A",
                    "text": "will start",
                    "translation": "시작할 것이다",
                },
                {
                    "id": "B",
                    "text": "will have started",
                    "translation": "이미 시작했을 것이다",
                },
                {"id": "C", "text": "starts", "translation": "시작한다"},
                {"id": "D", "text": "started", "translation": "시작했다"},
            ],
            "answer": "B",
            "explanation": "미래완료 ‘will have started’가 ‘~했을 것이다’ 의미.",
            "vocabulary": [
                {
                    "word": "conference",
                    "meaning": "회의",
                    "partOfSpeech": "noun",
                    "example": "The conference will be held in Seoul.",
                    "exampleTranslation": "회의는 서울에서 열릴 것이다.",
                }
            ],
        },
    ]

    # 문법 - 수일치
    grammar_subject_verb_agreement = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "수일치",
            "difficulty": "Medium",
            "questionText": "Either the manager or the assistants ___ responsible for locking the office.",
            "questionTranslation": "매니저나 어시스턴트 중 한 명이 사무실을 잠글 ___.",
            "choices": [
                {"id": "A", "text": "are", "translation": "이다"},
                {"id": "B", "text": "is", "translation": "이다"},
                {"id": "C", "text": "were", "translation": "였다"},
                {"id": "D", "text": "being", "translation": "되는 중이다"},
            ],
            "answer": "A",
            "explanation": "or 연결, 가까운 주어 assistants(복수) → are.",
            "vocabulary": [
                {
                    "word": "responsible",
                    "meaning": "책임 있는",
                    "partOfSpeech": "adjective",
                    "example": "She is responsible for the project.",
                    "exampleTranslation": "그녀는 그 프로젝트에 책임이 있다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "수일치",
            "difficulty": "Medium",
            "questionText": "A number of applicants ___ missing key documents.",
            "questionTranslation": "많은 지원자들이 핵심 서류를 ___ 있다.",
            "choices": [
                {"id": "A", "text": "is", "translation": "이다"},
                {"id": "B", "text": "are", "translation": "이다"},
                {"id": "C", "text": "was", "translation": "였다"},
                {"id": "D", "text": "has been", "translation": "되어 왔다"},
            ],
            "answer": "B",
            "explanation": "‘A number of + 복수’ → 복수 동사 are.",
            "vocabulary": [
                {
                    "word": "applicant",
                    "meaning": "지원자",
                    "partOfSpeech": "noun",
                    "example": "Each applicant must submit a resume.",
                    "exampleTranslation": "각 지원자는 이력서를 제출해야 한다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "수일치",
            "difficulty": "Medium",
            "questionText": "The committee ___ planning its annual retreat.",
            "questionTranslation": "위원회는 연례 워크숍을 계획 ___ 중이다.",
            "choices": [
                {"id": "A", "text": "are", "translation": "이다"},
                {"id": "B", "text": "is", "translation": "이다"},
                {"id": "C", "text": "be", "translation": "…"},
                {"id": "D", "text": "were", "translation": "였다"},
            ],
            "answer": "B",
            "explanation": "committee 집합명사, 단수로 취급 → is.",
            "vocabulary": [
                {
                    "word": "retreat",
                    "meaning": "워크숍/연수",
                    "partOfSpeech": "noun",
                    "example": "The team attended a retreat last month.",
                    "exampleTranslation": "팀은 지난달 연수에 참석했다.",
                }
            ],
        },
    ]
    # 문법 - 태(수동/능동)
    grammar_voice = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "태(수동/능동)",
            "difficulty": "Medium",
            "questionText": "The report ___ by the accounting department every quarter.",
            "questionTranslation": "그 보고서는 회계 부서에서 매 분기 ___ 된다.",
            "choices": [
                {"id": "A", "text": "prepares", "translation": "준비한다"},
                {"id": "B", "text": "is prepared", "translation": "준비된다"},
                {"id": "C", "text": "prepared", "translation": "준비했다"},
                {
                    "id": "D",
                    "text": "has prepared",
                    "translation": "준비해 왔다",
                },
            ],
            "answer": "B",
            "explanation": "행위자 accounting dept → 수동 ‘is prepared’.",
            "vocabulary": [
                {
                    "word": "quarter",
                    "meaning": "분기",
                    "partOfSpeech": "noun",
                    "example": "The company releases earnings every quarter.",
                    "exampleTranslation": "회사는 매 분기마다 실적을 발표한다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "태(수동/능동)",
            "difficulty": "Medium",
            "questionText": "The CEO will ___ the keynote speech tomorrow.",
            "questionTranslation": "CEO가 내일 기조연설을 ___ 것이다.",
            "choices": [
                {"id": "A", "text": "be delivered", "translation": "전달될"},
                {"id": "B", "text": "deliver", "translation": "전달하다"},
                {"id": "C", "text": "delivered", "translation": "전달했다"},
                {"id": "D", "text": "delivering", "translation": "전달하는 중"},
            ],
            "answer": "B",
            "explanation": "CEO가 행위자 → 능동 ‘deliver’.",
            "vocabulary": [
                {
                    "word": "keynote",
                    "meaning": "기조",
                    "partOfSpeech": "noun",
                    "example": "She gave the keynote address at the conference.",
                    "exampleTranslation": "그녀는 회의에서 기조연설을 했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "태(수동/능동)",
            "difficulty": "Medium",
            "questionText": "Customer feedback forms ___ after each workshop.",
            "questionTranslation": "워크숍마다 고객 피드백 양식이 ___ 된다.",
            "choices": [
                {"id": "A", "text": "collect", "translation": "수집한다"},
                {"id": "B", "text": "are collected", "translation": "수집된다"},
                {
                    "id": "C",
                    "text": "were collecting",
                    "translation": "수집하고 있었다",
                },
                {
                    "id": "D",
                    "text": "has collected",
                    "translation": "수집해 왔다",
                },
            ],
            "answer": "B",
            "explanation": "forms(목적어) → 수동 ‘are collected’.",
            "vocabulary": [
                {
                    "word": "feedback",
                    "meaning": "피드백",
                    "partOfSpeech": "noun",
                    "example": "We received positive feedback from customers.",
                    "exampleTranslation": "우리는 고객들로부터 긍정적인 피드백을 받았다.",
                }
            ],
        },
    ]
    # 문법 - 관계사
    grammar_relative_clause = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "관계사",
            "difficulty": "Medium",
            "questionText": "The intern ___ laptop was stolen will receive a replacement.",
            "questionTranslation": "노트북을 도난당한 인턴은 교체품을 받을 것이다.",
            "choices": [
                {"id": "A", "text": "who", "translation": "who"},
                {"id": "B", "text": "whose", "translation": "whose"},
                {"id": "C", "text": "whom", "translation": "whom"},
                {"id": "D", "text": "which", "translation": "which"},
            ],
            "answer": "B",
            "explanation": "소유격 관계대명사로 ‘whose’가 필요.",
            "vocabulary": [
                {
                    "word": "replacement",
                    "meaning": "교체품",
                    "partOfSpeech": "noun",
                    "example": "The company sent a replacement for the broken item.",
                    "exampleTranslation": "회사는 고장난 물건의 교체품을 보냈다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "관계사",
            "difficulty": "Medium",
            "questionText": "This is the contract ___ was signed yesterday.",
            "questionTranslation": "이것은 어제 서명된 계약서이다.",
            "choices": [
                {"id": "A", "text": "who", "translation": "who"},
                {"id": "B", "text": "that", "translation": "that"},
                {"id": "C", "text": "where", "translation": "where"},
                {"id": "D", "text": "when", "translation": "when"},
            ],
            "answer": "B",
            "explanation": "선행사가 사물 + 주격 → that.",
            "vocabulary": [
                {
                    "word": "contract",
                    "meaning": "계약서",
                    "partOfSpeech": "noun",
                    "example": "They signed the contract last week.",
                    "exampleTranslation": "그들은 지난주에 계약서에 서명했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "관계사",
            "difficulty": "Medium",
            "questionText": "The factory ___ the inspection took place is located in Busan.",
            "questionTranslation": "점검이 이루어진 공장은 부산에 위치해 있다.",
            "choices": [
                {"id": "A", "text": "which", "translation": "which"},
                {"id": "B", "text": "whom", "translation": "whom"},
                {"id": "C", "text": "where", "translation": "where"},
                {"id": "D", "text": "that", "translation": "that"},
            ],
            "answer": "C",
            "explanation": "장소 + ‘~한 곳’ 의미 → 관계부사 where.",
            "vocabulary": [
                {
                    "word": "inspection",
                    "meaning": "점검",
                    "partOfSpeech": "noun",
                    "example": "The inspection was completed successfully.",
                    "exampleTranslation": "점검이 성공적으로 완료되었다.",
                }
            ],
        },
    ]
    # 문법 - 비교구문
    grammar_comparative = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "비교구문",
            "difficulty": "Medium",
            "questionText": "This quarter’s profits are ___ than we projected.",
            "questionTranslation": "이번 분기 수익은 우리가 예상했던 것보다 ___.",
            "choices": [
                {"id": "A", "text": "high", "translation": "높다"},
                {"id": "B", "text": "highest", "translation": "가장 높다"},
                {"id": "C", "text": "higher", "translation": "더 높다"},
                {"id": "D", "text": "highly", "translation": "높게"},
            ],
            "answer": "C",
            "explanation": "비교급 문맥 → higher.",
            "vocabulary": [
                {
                    "word": "profit",
                    "meaning": "수익",
                    "partOfSpeech": "noun",
                    "example": "The company reported high profits this year.",
                    "exampleTranslation": "회사는 올해 높은 수익을 보고했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "비교구문",
            "difficulty": "Medium",
            "questionText": "Digital ads are becoming almost as effective ___ TV commercials.",
            "questionTranslation": "디지털 광고는 TV 광고만큼 거의 효과적이 되고 있다.",
            "choices": [
                {"id": "A", "text": "that", "translation": "that"},
                {"id": "B", "text": "like", "translation": "like"},
                {"id": "C", "text": "as", "translation": "as"},
                {"id": "D", "text": "than", "translation": "than"},
            ],
            "answer": "C",
            "explanation": "as + 형용사 + as 구조.",
            "vocabulary": [
                {
                    "word": "effective",
                    "meaning": "효과적인",
                    "partOfSpeech": "adjective",
                    "example": "The new strategy was very effective.",
                    "exampleTranslation": "새 전략은 매우 효과적이었다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "비교구문",
            "difficulty": "Medium",
            "questionText": "The new printer operates ___ than the previous model.",
            "questionTranslation": "새 프린터는 이전 모델보다 ___ 작동한다.",
            "choices": [
                {"id": "A", "text": "quiet", "translation": "조용하게"},
                {"id": "B", "text": "quieter", "translation": "더 조용하게"},
                {"id": "C", "text": "quietest", "translation": "가장 조용하게"},
                {"id": "D", "text": "quietly", "translation": "조용히"},
            ],
            "answer": "B",
            "explanation": "부사 비교급 → quieter.",
            "vocabulary": [
                {
                    "word": "operate",
                    "meaning": "작동하다",
                    "partOfSpeech": "verb",
                    "example": "The machine operates smoothly.",
                    "exampleTranslation": "기계가 부드럽게 작동한다.",
                }
            ],
        },
    ]
    # 문법 - 가정법
    grammar_conditional = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "가정법",
            "difficulty": "Medium",
            "questionText": "If we ___ more time, we would conduct additional tests.",
            "questionTranslation": "시간이 더 있다면, 우리는 추가 테스트를 할 텐데.",
            "choices": [
                {"id": "A", "text": "have", "translation": "가진다"},
                {"id": "B", "text": "had", "translation": "가졌다면"},
                {"id": "C", "text": "will have", "translation": "가질 것이다"},
                {"id": "D", "text": "having", "translation": "갖고"},
            ],
            "answer": "B",
            "explanation": "가정법 과거: If + 과거, would + 원형.",
            "vocabulary": [
                {
                    "word": "conduct",
                    "meaning": "실시하다",
                    "partOfSpeech": "verb",
                    "example": "The company will conduct a survey.",
                    "exampleTranslation": "회사가 설문조사를 실시할 것이다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "가정법",
            "difficulty": "Medium",
            "questionText": "Had the delivery arrived on time, we ___ the product launch.",
            "questionTranslation": "배송이 제시간에 도착했다면, 우리는 제품 출시를 ___ 것이다.",
            "choices": [
                {
                    "id": "A",
                    "text": "will proceed",
                    "translation": "진행할 것이다",
                },
                {
                    "id": "B",
                    "text": "would have proceeded",
                    "translation": "진행했을 것이다",
                },
                {"id": "C", "text": "proceeded", "translation": "진행했다"},
                {
                    "id": "D",
                    "text": "would proceed",
                    "translation": "진행할 텐데",
                },
            ],
            "answer": "B",
            "explanation": "가정법 과거완료: Had + p.p, would have + p.p.",
            "vocabulary": [
                {
                    "word": "proceed",
                    "meaning": "진행하다",
                    "partOfSpeech": "verb",
                    "example": "The meeting will proceed as planned.",
                    "exampleTranslation": "회의는 예정대로 진행될 것이다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "가정법",
            "difficulty": "Medium",
            "questionText": "If Ms. Lee were here, she ___ the negotiations.",
            "questionTranslation": "이 씨가 여기 있다면, 그녀가 협상을 ___ 것이다.",
            "choices": [
                {
                    "id": "A",
                    "text": "will handle",
                    "translation": "처리할 것이다",
                },
                {
                    "id": "B",
                    "text": "would handle",
                    "translation": "처리할 텐데",
                },
                {"id": "C", "text": "handled", "translation": "처리했다"},
                {"id": "D", "text": "handles", "translation": "처리한다"},
            ],
            "answer": "B",
            "explanation": "가정법 과거: were + would + 동사.",
            "vocabulary": [
                {
                    "word": "negotiation",
                    "meaning": "협상",
                    "partOfSpeech": "noun",
                    "example": "The negotiation between the companies was successful.",
                    "exampleTranslation": "회사들 간의 협상이 성공적이었다.",
                }
            ],
        },
    ]
    # 문법 - 부정사/동명사
    grammar_infinitive_gerund = [
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "부정사/동명사",
            "difficulty": "Medium",
            "questionText": "The supervisor encouraged staff ___ the new software.",
            "questionTranslation": "상사는 직원들에게 새 소프트웨어를 ___ 권장했다.",
            "choices": [
                {"id": "A", "text": "to install", "translation": "설치하도록"},
                {
                    "id": "B",
                    "text": "installing",
                    "translation": "설치하는 것을",
                },
                {"id": "C", "text": "install", "translation": "설치하다"},
                {"id": "D", "text": "installed", "translation": "설치된"},
            ],
            "answer": "A",
            "explanation": "encourage + 목적어 + to 부정사.",
            "vocabulary": [
                {
                    "word": "install",
                    "meaning": "설치하다",
                    "partOfSpeech": "verb",
                    "example": "Please install the latest version of the software.",
                    "exampleTranslation": "최신 버전의 소프트웨어를 설치해 주세요.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "부정사/동명사",
            "difficulty": "Medium",
            "questionText": "She denied ___ the confidential file.",
            "questionTranslation": "그녀는 기밀 파일을 ___ 부인했다.",
            "choices": [
                {"id": "A", "text": "to read", "translation": "읽는 것을"},
                {"id": "B", "text": "reading", "translation": "읽었다고"},
                {"id": "C", "text": "read", "translation": "읽다"},
                {"id": "D", "text": "to have read", "translation": "읽었음을"},
            ],
            "answer": "B",
            "explanation": "deny + 동명사.",
            "vocabulary": [
                {
                    "word": "confidential",
                    "meaning": "기밀의",
                    "partOfSpeech": "adjective",
                    "example": "The company keeps all client information confidential.",
                    "exampleTranslation": "회사는 모든 고객 정보를 기밀로 유지한다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "문법",
            "questionSubType": "부정사/동명사",
            "difficulty": "Medium",
            "questionText": "It is important ___ all fields in the form.",
            "questionTranslation": "양식의 모든 칸을 ___ 것이 중요하다.",
            "choices": [
                {"id": "A", "text": "complete", "translation": "작성하다"},
                {
                    "id": "B",
                    "text": "to complete",
                    "translation": "작성하는 것",
                },
                {"id": "C", "text": "completing", "translation": "작성하기"},
                {"id": "D", "text": "completed", "translation": "작성된"},
            ],
            "answer": "B",
            "explanation": "It is important + to 부정사.",
            "vocabulary": [
                {
                    "word": "field",
                    "meaning": "칸/항목",
                    "partOfSpeech": "noun",
                    "example": "Please fill in all the fields on the form.",
                    "exampleTranslation": "양식의 모든 칸을 작성해 주세요.",
                }
            ],
        },
    ]
    # 어휘 - 동의어
    vocabulary_synonym = [
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "동의어",
            "difficulty": "Medium",
            "questionText": "The CEO delivered a brief but ___ speech.",
            "questionTranslation": "CEO는 짧지만 ___ 연설을 했다.",
            "choices": [
                {"id": "A", "text": "concise", "translation": "간결한"},
                {"id": "B", "text": "lengthy", "translation": "장황한"},
                {"id": "C", "text": "tedious", "translation": "지루한"},
                {"id": "D", "text": "vague", "translation": "모호한"},
            ],
            "answer": "A",
            "explanation": "brief와 의미 유사한 'concise'가 정답.",
            "vocabulary": [
                {
                    "word": "concise",
                    "meaning": "간결한",
                    "partOfSpeech": "adjective",
                    "example": "Her explanation was clear and concise.",
                    "exampleTranslation": "그녀의 설명은 명확하고 간결했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "동의어",
            "difficulty": "Medium",
            "questionText": "The manager ___ the meeting to discuss the budget.",
            "questionTranslation": "매니저는 예산 논의를 위해 회의를 ___.",
            "choices": [
                {"id": "A", "text": "convened", "translation": "소집했다"},
                {"id": "B", "text": "cancelled", "translation": "취소했다"},
                {"id": "C", "text": "delayed", "translation": "연기했다"},
                {"id": "D", "text": "ignored", "translation": "무시했다"},
            ],
            "answer": "A",
            "explanation": "'convened' = called, assembled.",
            "vocabulary": [
                {
                    "word": "convene",
                    "meaning": "소집하다",
                    "partOfSpeech": "verb",
                    "example": "The board will convene next Monday.",
                    "exampleTranslation": "이사회는 다음 주 월요일에 소집될 것이다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "동의어",
            "difficulty": "Medium",
            "questionText": "After months of ___, the two firms finally merged.",
            "questionTranslation": "수개월의 ___ 끝에 두 회사가 마침내 합병했다.",
            "choices": [
                {"id": "A", "text": "negotiation", "translation": "협상"},
                {"id": "B", "text": "competition", "translation": "경쟁"},
                {"id": "C", "text": "celebration", "translation": "축하"},
                {"id": "D", "text": "litigation", "translation": "소송"},
            ],
            "answer": "A",
            "explanation": "'negotiation'과 합병 맥락 상 일치.",
            "vocabulary": [
                {
                    "word": "merge",
                    "meaning": "합병하다",
                    "partOfSpeech": "verb",
                    "example": "The companies decided to merge last year.",
                    "exampleTranslation": "그 회사들은 지난해 합병하기로 결정했다.",
                }
            ],
        },
    ]
    # 어휘 - 반의어
    vocabulary_antonym = [
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "반의어",
            "difficulty": "Medium",
            "questionText": "The instructions were so ___ that many users were confused.",
            "questionTranslation": "지침이 너무 ___ 해서 많은 사용자가 혼란스러웠다.",
            "choices": [
                {"id": "A", "text": "clear", "translation": "명확한"},
                {"id": "B", "text": "precise", "translation": "정확한"},
                {"id": "C", "text": "ambiguous", "translation": "모호한"},
                {"id": "D", "text": "explicit", "translation": "분명한"},
            ],
            "answer": "C",
            "explanation": "'ambiguous'는 clear의 반의어.",
            "vocabulary": [
                {
                    "word": "ambiguous",
                    "meaning": "모호한",
                    "partOfSpeech": "adjective",
                    "example": "The wording of the contract is ambiguous.",
                    "exampleTranslation": "계약서의 문구가 모호하다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "반의어",
            "difficulty": "Medium",
            "questionText": "Unlike his predecessor, the new director prefers a ___ schedule.",
            "questionTranslation": "전임자와 달리 새 이사는 ___ 일정을 선호한다.",
            "choices": [
                {"id": "A", "text": "rigid", "translation": "엄격한"},
                {"id": "B", "text": "flexible", "translation": "유연한"},
                {"id": "C", "text": "annual", "translation": "연례의"},
                {"id": "D", "text": "temporary", "translation": "임시의"},
            ],
            "answer": "B",
            "explanation": "rigid ↔ flexible.",
            "vocabulary": [
                {
                    "word": "predecessor",
                    "meaning": "전임자",
                    "partOfSpeech": "noun",
                    "example": "The new manager replaced his predecessor last month.",
                    "exampleTranslation": "새 매니저가 지난달 전임자를 교체했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "반의어",
            "difficulty": "Medium",
            "questionText": "The proposal was rejected because it was deemed ___ to company goals.",
            "questionTranslation": "그 제안은 회사 목표와 ___ 것으로 간주되어 거절되었다.",
            "choices": [
                {"id": "A", "text": "contrary", "translation": "반대되는"},
                {"id": "B", "text": "aligned", "translation": "일치하는"},
                {"id": "C", "text": "similar", "translation": "유사한"},
                {"id": "D", "text": "complementary", "translation": "보완적인"},
            ],
            "answer": "A",
            "explanation": "aligned의 반대 = contrary.",
            "vocabulary": [
                {
                    "word": "contrary",
                    "meaning": "반대의",
                    "partOfSpeech": "adjective",
                    "example": "His opinion is contrary to the majority.",
                    "exampleTranslation": "그의 의견은 대다수와 반대이다.",
                }
            ],
        },
    ]
    # 어휘 - 관용표현
    vocabulary_idiom = [
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "관용표현",
            "difficulty": "Medium",
            "questionText": "We should keep the new policy ___ until it is approved.",
            "questionTranslation": "새 정책이 승인될 때까지는 ___ 유지해야 한다.",
            "choices": [
                {"id": "A", "text": "under wraps", "translation": "비밀로"},
                {"id": "B", "text": "on the house", "translation": "무료로"},
                {"id": "C", "text": "out of line", "translation": "엉뚱하게"},
                {"id": "D", "text": "up in the air", "translation": "미정으로"},
            ],
            "answer": "A",
            "explanation": "‘keep something under wraps’ = 비밀로 하다.",
            "vocabulary": [
                {
                    "word": "approve",
                    "meaning": "승인하다",
                    "partOfSpeech": "verb",
                    "example": "The manager approved the new policy.",
                    "exampleTranslation": "매니저가 새 정책을 승인했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "관용표현",
            "difficulty": "Medium",
            "questionText": "The CEO’s sudden resignation caught everyone ___.",
            "questionTranslation": "CEO의 갑작스런 사임은 모두를 ___ 했다.",
            "choices": [
                {
                    "id": "A",
                    "text": "by surprise",
                    "translation": "깜짝 놀라게",
                },
                {"id": "B", "text": "in charge", "translation": "책임지게"},
                {"id": "C", "text": "on duty", "translation": "근무 중"},
                {"id": "D", "text": "at large", "translation": "잡히지 않은"},
            ],
            "answer": "A",
            "explanation": "catch someone by surprise = 예상치 못하게 하다.",
            "vocabulary": [
                {
                    "word": "resignation",
                    "meaning": "사임",
                    "partOfSpeech": "noun",
                    "example": "She handed in her resignation yesterday.",
                    "exampleTranslation": "그녀는 어제 사임서를 제출했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "관용표현",
            "difficulty": "Medium",
            "questionText": "The marketing plan is still ___; we need more data.",
            "questionTranslation": "마케팅 계획은 아직 ___; 더 많은 데이터가 필요하다.",
            "choices": [
                {
                    "id": "A",
                    "text": "a piece of cake",
                    "translation": "식은 죽",
                },
                {
                    "id": "B",
                    "text": "up in the air",
                    "translation": "미정 상태",
                },
                {
                    "id": "C",
                    "text": "behind the scenes",
                    "translation": "막후에서",
                },
                {
                    "id": "D",
                    "text": "under the weather",
                    "translation": "몸이 안 좋은",
                },
            ],
            "answer": "B",
            "explanation": "up in the air = 결정되지 않은.",
            "vocabulary": [
                {
                    "word": "data",
                    "meaning": "데이터",
                    "partOfSpeech": "noun",
                    "example": "We need more data to make a decision.",
                    "exampleTranslation": "결정을 내리기 위해 더 많은 데이터가 필요하다.",
                }
            ],
        },
    ]
    # 어휘 - Collocation
    vocabulary_collocation = [
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "Collocation",
            "difficulty": "Medium",
            "questionText": "The board will ___ a vote on the merger next week.",
            "questionTranslation": "이사회는 다음 주 합병에 대해 표결을 ___ 것이다.",
            "choices": [
                {"id": "A", "text": "take", "translation": "실시하다"},
                {"id": "B", "text": "do", "translation": "하다"},
                {"id": "C", "text": "make", "translation": "만들다"},
                {"id": "D", "text": "set", "translation": "설정하다"},
            ],
            "answer": "A",
            "explanation": "‘take a vote’가 자연스러운 연어.",
            "vocabulary": [
                {
                    "word": "merger",
                    "meaning": "합병",
                    "partOfSpeech": "noun",
                    "example": "The merger was approved by the board.",
                    "exampleTranslation": "합병이 이사회에서 승인되었다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "Collocation",
            "difficulty": "Medium",
            "questionText": "Please ___ an effort to arrive on time.",
            "questionTranslation": "제시간에 도착하도록 ___ 해 주세요.",
            "choices": [
                {"id": "A", "text": "do", "translation": "하다"},
                {"id": "B", "text": "make", "translation": "기울이다"},
                {"id": "C", "text": "take", "translation": "취하다"},
                {"id": "D", "text": "give", "translation": "주다"},
            ],
            "answer": "B",
            "explanation": "make an effort = 노력하다.",
            "vocabulary": [
                {
                    "word": "effort",
                    "meaning": "노력",
                    "partOfSpeech": "noun",
                    "example": "She made an effort to finish the project early.",
                    "exampleTranslation": "그녀는 프로젝트를 일찍 끝내려고 노력했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "Collocation",
            "difficulty": "Medium",
            "questionText": "Our company aims to ___ strong relationships with clients.",
            "questionTranslation": "우리 회사는 고객과 강한 관계를 ___ 것이 목표이다.",
            "choices": [
                {"id": "A", "text": "build", "translation": "구축하다"},
                {"id": "B", "text": "raise", "translation": "올리다"},
                {"id": "C", "text": "lift", "translation": "들어올리다"},
                {"id": "D", "text": "arise", "translation": "생기다"},
            ],
            "answer": "A",
            "explanation": "build relationships = 관계를 구축하다.",
            "vocabulary": [
                {
                    "word": "aim",
                    "meaning": "목표로 하다",
                    "partOfSpeech": "verb",
                    "example": "We aim to improve customer satisfaction.",
                    "exampleTranslation": "우리는 고객 만족도를 높이는 것을 목표로 한다.",
                }
            ],
        },
    ]

    # 어휘 - phrasal verb
    vocabulary_phrasal_verb = [
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "phrasal verb",
            "difficulty": "Medium",
            "questionText": "The manager asked the team to ___ their ideas for the project.",
            "questionTranslation": "매니저는 팀에게 프로젝트에 대한 아이디어를 ___ 해 달라고 했다.",
            "choices": [
                {"id": "A", "text": "come up with", "translation": "생각해 내다"},
                {"id": "B", "text": "give up", "translation": "포기하다"},
                {"id": "C", "text": "look into", "translation": "조사하다"},
                {"id": "D", "text": "put off", "translation": "미루다"},
            ],
            "answer": "A",
            "explanation": "'come up with' = 생각해 내다.",
            "vocabulary": [
                {
                    "word": "idea",
                    "meaning": "아이디어",
                    "partOfSpeech": "noun",
                    "example": "She came up with a great idea.",
                    "exampleTranslation": "그녀는 훌륭한 아이디어를 생각해 냈다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "phrasal verb",
            "difficulty": "Medium",
            "questionText": "The new policy will ___ next month.",
            "questionTranslation": "새 정책은 다음 달에 ___ 것이다.",
            "choices": [
                {"id": "A", "text": "take effect", "translation": "효력을 발휘하다"},
                {"id": "B", "text": "put off", "translation": "미루다"},
                {"id": "C", "text": "give in", "translation": "양보하다"},
                {"id": "D", "text": "turn down", "translation": "거절하다"},
            ],
            "answer": "A",
            "explanation": "'take effect' = 효력을 발휘하다.",
            "vocabulary": [
                {
                    "word": "policy",
                    "meaning": "정책",
                    "partOfSpeech": "noun",
                    "example": "The new policy will take effect next month.",
                    "exampleTranslation": "새 정책은 다음 달에 효력을 발휘할 것이다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "어휘",
            "questionSubType": "phrasal verb",
            "difficulty": "Medium",
            "questionText": "The team needs to ___ the deadline for the project.",
            "questionTranslation": "팀은 프로젝트의 마감일을 ___ 필요가 있다.",
            "choices": [
                {"id": "A", "text": "put off", "translation": "미루다"},
                {"id": "B", "text": "bring up", "translation": "제기하다"},
                {"id": "C", "text": "carry out", "translation": "실행하다"},
                {"id": "D", "text": "set up", "translation": "설정하다"},
            ],
            "answer": "D",
            "explanation": "'set up' = 설정하다.",
            "vocabulary": [
                {
                    "word": "deadline",
                    "meaning": "마감일",
                    "partOfSpeech": "noun",
                    "example": "The deadline for the project is next Friday.",
                    "exampleTranslation": "프로젝트의 마감일은 다음 주 금요일이다.",
                }
            ],
        },
    ]
    # 전치사/접속사/접속부사 - 시간/장소 전치사
    preposition_time_place = [
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "시간/장소 전치사",
            "difficulty": "Medium",
            "questionText": "The meeting is scheduled for ___ 3 PM.",
            "questionTranslation": "회의는 ___ 오후 3시에 예정되어 있다.",
            "choices": [
                {"id": "A", "text": "in", "translation": "안에"},
                {"id": "B", "text": "on", "translation": "위에"},
                {"id": "C", "text": "at", "translation": "에서"},
                {"id": "D", "text": "to", "translation": "로"},
            ],
            "answer": "C",
            "explanation": "'at' = 특정 시간에.",
            "vocabulary": [
                {
                    "word": "meeting",
                    "meaning": "회의",
                    "partOfSpeech": "noun",
                    "example": "The meeting will start at 3 PM.",
                    "exampleTranslation": "회의는 오후 3시에 시작할 것이다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "시간/장소 전치사",
            "difficulty": "Medium",
            "questionText": "The report is due ___ Friday.",
            "questionTranslation": "보고서는 금요일에 ___ 예정이다.",
            "choices": [
                {"id": "A", "text": "in", "translation": "안에"},
                {"id": "B", "text": "on", "translation": "위에"},
                {"id": "C", "text": "at", "translation": "에서"},
                {"id": "D", "text": "to", "translation": "로"},
            ],
            "answer": "B",
            "explanation": "'on' = 특정 날짜에.",
            "vocabulary": [
                {
                    "word": "report",
                    "meaning": "보고서",
                    "partOfSpeech": "noun",
                    "example": "The report is due on Friday.",
                    "exampleTranslation": "보고서는 금요일까지 제출해야 한다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "시간/장소 전치사",
            "difficulty": "Medium",
            "questionText": "The conference will be held ___ the downtown area.",
            "questionTranslation": "회의는 ___ 시내 지역에서 열릴 것이다.",
            "choices": [
                {"id": "A", "text": "in", "translation": "안에"},
                {"id": "B", "text": "on", "translation": "위에"},
                {"id": "C", "text": "at", "translation": "에서"},
                {"id": "D", "text": "to", "translation": "로"},
            ],
            "answer": "A",
            "explanation": "'in' = 특정 장소에.",
            "vocabulary": [
                {
                    "word": "conference",
                    "meaning": "회의",
                    "partOfSpeech": "noun",
                    "example": "The conference will be held in the downtown area.",
                    "exampleTranslation": "회의는 시내 지역에서 열릴 것이다.",
                }
            ],
        },
    ]

    # 전치사/접속사/접속부사 - 원인/결과
    conjunction_cause_effect = [
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "원인/결과",
            "difficulty": "High",
            "questionText": "The company achieved record sales ___ the economic downturn.",
            "questionTranslation": "경기 침체에도 불구하고 회사는 기록적인 매출을 달성했다.",
            "choices": [
                {"id": "A", "text": "despite", "translation": "~에도 불구하고"},
                {"id": "B", "text": "because of", "translation": "~때문에"},
                {"id": "C", "text": "due to", "translation": "~때문에"},
                {"id": "D", "text": "as a result of", "translation": "~의 결과로"},
            ],
            "answer": "A",
            "explanation": "'despite'는 ~에도 불구하고라는 의미로, 역접 관계를 나타냄.",
            "vocabulary": [
                {
                    "word": "downturn",
                    "meaning": "경기 침체",
                    "partOfSpeech": "noun",
                    "example": "The company survived the economic downturn.",
                    "exampleTranslation": "회사는 경기 침체를 견뎌냈다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "원인/결과",
            "difficulty": "High",
            "questionText": "___ his outstanding performance, Mr. Kim was promoted to manager.",
            "questionTranslation": "김 씨는 뛰어난 실적 ___ 매니저로 승진했다.",
            "choices": [
                {"id": "A", "text": "Because of", "translation": "~때문에"},
                {"id": "B", "text": "In spite of", "translation": "~에도 불구하고"},
                {"id": "C", "text": "Although", "translation": "~이지만"},
                {"id": "D", "text": "Whereas", "translation": "~인 반면에"},
            ],
            "answer": "A",
            "explanation": "'Because of'는 ~때문에라는 의미로, 원인·이유를 나타냄.",
            "vocabulary": [
                {
                    "word": "outstanding",
                    "meaning": "뛰어난",
                    "partOfSpeech": "adjective",
                    "example": "She received an award for her outstanding work.",
                    "exampleTranslation": "그녀는 뛰어난 업무로 상을 받았다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "원인/결과",
            "difficulty": "High",
            "questionText": "The shipment was delayed ___ a strike at the port.",
            "questionTranslation": "항구의 파업 ___ 배송이 지연되었다.",
            "choices": [
                {"id": "A", "text": "because of", "translation": "~때문에"},
                {"id": "B", "text": "despite", "translation": "~에도 불구하고"},
                {"id": "C", "text": "although", "translation": "~이지만"},
                {"id": "D", "text": "even though", "translation": "~임에도 불구하고"},
            ],
            "answer": "A",
            "explanation": "'because of'는 ~때문에라는 의미로, 원인·이유를 명확히 나타냄.",
            "vocabulary": [
                {
                    "word": "strike",
                    "meaning": "파업",
                    "partOfSpeech": "noun",
                    "example": "The workers went on strike for better pay.",
                    "exampleTranslation": "노동자들은 더 나은 임금을 위해 파업에 들어갔다.",
                }
            ],
        },
    ]

    # 전치사/접속사/접속부사 - 양보
    conjunction_concession = [
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "양보",
            "difficulty": "High",
            "questionText": "___ the challenges, the team completed the project on time.",
            "questionTranslation": "어려움에도 불구하고 팀은 프로젝트를 제시간에 완료했다.",
            "choices": [
                {"id": "A", "text": "In spite of", "translation": "~에도 불구하고"},
                {"id": "B", "text": "Because of", "translation": "~때문에"},
                {"id": "C", "text": "Due to", "translation": "~때문에"},
                {"id": "D", "text": "Although", "translation": "~이지만"},
            ],
            "answer": "A",
            "explanation": "'In spite of'는 ~에도 불구하고라는 의미로, 역접 관계를 나타냄.",
            "vocabulary": [
                {
                    "word": "challenge",
                    "meaning": "어려움",
                    "partOfSpeech": "noun",
                    "example": "We faced many challenges during the project.",
                    "exampleTranslation": "우리는 프로젝트 동안 많은 어려움에 직면했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "양보",
            "difficulty": "High",
            "questionText": "___ the rain, the event will proceed as planned.",
            "questionTranslation": "비가 ___ 행사 진행은 예정대로 진행된다.",
            "choices": [
                {"id": "A", "text": "Despite", "translation": "~에도 불구하고"},
                {"id": "B", "text": "Because of", "translation": "~때문에"},
                {"id": "C", "text": "Due to", "translation": "~때문에"},
                {"id": "D", "text": "Although", "translation": "~이지만"},
            ],
            "answer": "A",
            "explanation": "'Despite'는 ~에도 불구하고라는 의미로, 역접 관계를 나타냄.",
            "vocabulary": [
                {
                    "word": "event",
                    "meaning": "행사",
                    "partOfSpeech": "noun",
                    "example": "The event will start at 10 AM.",
                    "exampleTranslation": "행사는 오전 10시에 시작된다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "양보",
            "difficulty": "High",
            "questionText": "___ the difficulties, she managed to finish the report.",
            "questionTranslation": "어려움에도 불구하고 그녀는 보고서를 끝냈다.",
            "choices": [
                {"id": "A", "text": "In spite of", "translation": "~에도 불구하고"},
                {"id": "B", "text": "Because of", "translation": "~때문에"},
                {"id": "C", "text": "Due to", "translation": "~때문에"},
                {"id": "D", "text": "Although", "translation": "~이지만"},
            ],
            "answer": "A",
            "explanation": "'In spite of'는 ~에도 불구하고라는 의미로, 역접 관계를 나타냄.",
            "vocabulary": [
                {
                    "word": "manage",
                    "meaning": "해내다",
                    "partOfSpeech": "verb",
                    "example": "She managed to finish the task on time.",
                    "exampleTranslation": "그녀는 제시간에 과제를 해냈다.",
                }
            ],
        },
    ]
    # 전치사/접속사/접속부사 - 조건
    conjunction_condition = [
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "조건",
            "difficulty": "High",
            "questionText": "___ you finish the report, we can submit it tomorrow.",
            "questionTranslation": "보고서를 ___ 내일 제출할 수 있다.",
            "choices": [
                {"id": "A", "text": "If", "translation": "~라면"},
                {"id": "B", "text": "Unless", "translation": "~하지 않는 한"},
                {"id": "C", "text": "Although", "translation": "~이지만"},
                {"id": "D", "text": "In case of", "translation": "~의 경우에"},
            ],
            "answer": "A",
            "explanation": "'If'는 조건을 나타내는 접속사.",
            "vocabulary": [
                {
                    "word": "submit",
                    "meaning": "제출하다",
                    "partOfSpeech": "verb",
                    "example": "Please submit your application by Friday.",
                    "exampleTranslation": "금요일까지 지원서를 제출해 주세요.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "조건",
            "difficulty": "High",
            "questionText": "___ you need assistance, please call the help desk.",
            "questionTranslation": "도움이 ___ 필요하면, 헬프 데스크에 전화해 주세요.",
            "choices": [
                {"id": "A", "text": "If", "translation": "~라면"},
                {"id": "B", "text": "Unless", "translation": "~하지 않는 한"},
                {"id": "C", "text": "Although", "translation": "~이지만"},
                {"id": "D", "text": "In case of", "translation": "~의 경우에"},
            ],
            "answer": "A",
            "explanation": "'If'는 조건을 나타내는 접속사.",
            "vocabulary": [
                {
                    "word": "assistance",
                    "meaning": "도움",
                    "partOfSpeech": "noun",
                    "example": "She asked for assistance with the project.",
                    "exampleTranslation": "그녀는 프로젝트에 대한 도움을 요청했다.",
                }
            ],
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "조건",
            "difficulty": "High",
            "questionText": "___ it rains, the event will be postponed.",
            "questionTranslation": "비가 ___ 행사 연기될 것이다.",
            "choices": [
                {"id": "A", "text": "If", "translation": "~라면"},
                {"id": "B", "text": "Unless", "translation": "~하지 않는 한"},
                {"id": "C", "text": "Although", "translation": "~이지만"},
                {"id": "D", "text": "In case of", "translation": "~의 경우에"},
            ],
            "answer": "A",
            "explanation": "'If'는 조건을 나타내는 접속사.",
            "vocabulary": [
                {
                    "word": "postpone",
                    "meaning": "연기하다",
                    "partOfSpeech": "verb",
                    "example": "The meeting was postponed due to the weather.",
                    "exampleTranslation": "회의가 날씨 때문에 연기되었다.",
                }
            ],
        },
    ]

    # 전치사/접속사/접속부사 - 접속부사
    conjunction_preposition_conjunctive_adverb = [
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "접속부사",
            "difficulty": "High",
            "questionText": "The team worked overtime; ___, the project was completed on schedule.",
            "questionTranslation": "팀은 초과 근무를 했다; ___, 프로젝트는 예정대로 완료되었다.",
            "choices": [
                {"id": "A", "text": "however", "translation": "그러나"},
                {"id": "B", "text": "because", "translation": "왜냐하면"},
                {"id": "C", "text": "although", "translation": "비록 ~일지라도"},
                {"id": "D", "text": "since", "translation": "~이래로"},
            ],
            "answer": "A",
            "explanation": "'however'는 앞 문장과 대조되는 접속부사.",
            "vocabulary": [
                {
                    "word": "overtime",
                    "meaning": "초과 근무",
                    "partOfSpeech": "noun",
                    "example": "He often works overtime to meet deadlines.",
                    "exampleTranslation": "그는 마감일을 맞추기 위해 종종 초과 근무를 한다.",
                },
                {
                    "word": "schedule",
                    "meaning": "일정",
                    "partOfSpeech": "noun",
                    "example": "The meeting is on schedule.",
                    "exampleTranslation": "회의가 예정대로 진행된다.",
                },
            ],
            "example": "She was tired; however, she finished her work.",
            "exampleTranslation": "그녀는 피곤했지만 일을 끝냈다.",
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "접속부사",
            "difficulty": "High",
            "questionText": "The company expanded rapidly; ___, it faced several challenges.",
            "questionTranslation": "회사는 빠르게 확장했다; ___, 여러 도전에 직면했다.",
            "choices": [
                {"id": "A", "text": "nevertheless", "translation": "그럼에도 불구하고"},
                {"id": "B", "text": "because", "translation": "왜냐하면"},
                {"id": "C", "text": "unless", "translation": "~하지 않는 한"},
                {"id": "D", "text": "while", "translation": "~하는 동안"},
            ],
            "answer": "A",
            "explanation": "'nevertheless'는 앞 문장과 역접 관계를 나타내는 접속부사.",
            "vocabulary": [
                {
                    "word": "expand",
                    "meaning": "확장하다",
                    "partOfSpeech": "verb",
                    "example": "The company plans to expand into new markets.",
                    "exampleTranslation": "회사는 새로운 시장으로 확장할 계획이다.",
                },
                {
                    "word": "challenge",
                    "meaning": "도전",
                    "partOfSpeech": "noun",
                    "example": "Starting a new business is a big challenge.",
                    "exampleTranslation": "새로운 사업을 시작하는 것은 큰 도전이다.",
                },
            ],
            "example": "It was raining; nevertheless, they went for a walk.",
            "exampleTranslation": "비가 오고 있었지만 그들은 산책을 나갔다.",
        },
        {
            "part": 5,
            "questionCategory": "전치사/접속사/접속부사",
            "questionSubType": "접속부사",
            "difficulty": "High",
            "questionText": "The deadline is approaching; ___, all team members must submit their reports.",
            "questionTranslation": "마감일이 다가오고 있다; ___, 모든 팀원은 보고서를 제출해야 한다.",
            "choices": [
                {"id": "A", "text": "therefore", "translation": "그러므로"},
                {"id": "B", "text": "although", "translation": "비록 ~일지라도"},
                {"id": "C", "text": "because", "translation": "왜냐하면"},
                {"id": "D", "text": "unless", "translation": "~하지 않는 한"},
            ],
            "answer": "A",
            "explanation": "'therefore'는 앞의 원인에 대한 결과를 나타내는 접속부사.",
            "vocabulary": [
                {
                    "word": "approach",
                    "meaning": "다가오다",
                    "partOfSpeech": "verb",
                    "example": "The train is approaching the station.",
                    "exampleTranslation": "기차가 역에 다가오고 있다.",
                },
                {
                    "word": "submit",
                    "meaning": "제출하다",
                    "partOfSpeech": "verb",
                    "example": "Please submit your application by Friday.",
                    "exampleTranslation": "금요일까지 지원서를 제출해 주세요.",
                },
            ],
            "example": "He was the oldest; therefore, he was chosen as the leader.",
            "exampleTranslation": "그가 가장 나이가 많아서 리더로 뽑혔다.",
        },
    ]
