# Five-minute interview walkthrough

[Back to portfolio](../README.md)

## 0:00–0:45 — Frame the business problem

Explain how a shelter must coordinate clinical, ownership and suitability evidence before listing an animal. Show the [business case](business-case.md). Identify the two workflows and the responsibilities of staff, veterinarians, adopters and the external registry.

## 0:45–1:45 — Show requirements analysis

Open [FUS2 and FUS7](requirements.md). Explain why a Boolean urgent-treatment flag needs a decision owner, reason, treatment plan and reassessment. Then show how the latest medical check controls release. Use the exact criterion IDs to make the rules reviewable.

## 1:45–2:45 — Explain concurrency and exception handling

Open [AD1](../assets/diagrams/AD1_part1.png) and [AD2](../assets/diagrams/AD2_part2.png). Explain that a join proves completion, while eligibility requires separate decision conditions. Walk through a failed check and its recovery path.

## 2:45–3:45 — Connect behaviour to state and data

Show the [state machine](../assets/diagrams/SM_full.png) and the [class model](../assets/diagrams/CL_part2.png). Explain why Adopted and Released differ, what Release Paused preserves, and which AdoptionRecord fields support this distinction. Follow the [FUS7 worked example](traceability.md).

## 3:45–4:30 — Discuss quality and trade-offs

Use NFUS3, NFUS4 and NFUS6 to explain measurable performance, recovery and integrity requirements. State that the numbers are proposed targets. Identify an unresolved design issue such as competing applications or prolonged release pauses, and describe what stakeholders must confirm.

## 4:30–5:00 — Bound the evidence

Show the [native validation evidence](evidence/README.md). Explain what the integrity and UML checks establish, and why semantic review and runtime acceptance still matter. State your responsibility and the substantive AI-assisted revision scope clearly.

## 中文口說提示

「這個專案的重點是把收容所的業務規則轉成可追蹤、可測試的系統設計。我負責需求分析、UML 與報告；修訂版使用 AI 協助檢查與修改。最值得說明的決策，是把『完成領養』和『動物實際離所』分開，並讓最新健康檢查決定能否交付。我可以從驗收條件一路對照流程、互動、狀態與資料模型，也能指出仍需利害關係人確認的假設。」
