# PawPath｜商業資訊系統分析與設計

**需求分析 · 業務流程建模 · UML · 領域模型 · Enterprise Architect · 驗收條件**

動物收容所如何協調入所、醫療、所有權與領養審查，避免尚未符合資格的動物被公開上架，或在最後健康檢查前離所？

PawPath 將這個業務問題整理為 **14 則使用者故事、84 項驗收條件與七張相互對照的 UML 圖**，涵蓋入所、醫療放行、申請審查、完成領養、實際離所及後續追蹤。

**[English](README.md) · [個案與設計成果](docs/case-study.md) · [業務分析](docs/business-case.md) · [完整需求](docs/requirements.md) · [UML 模型成果](docs/model-gallery.md)**

![PawPath 從入所到安全交付的設計概覽](assets/design-overview.svg)

## 完成的分析與設計成果

| 作業成果 | 具體結果 | 成果證據 |
| --- | --- | --- |
| 需求規格 | 7 則功能與 7 則非功能使用者故事，每則 6 項驗收條件，共 **84 項 AC** | [需求目錄](docs/requirements.md)、[驗收條件資料集](analysis/acceptance-criteria.csv) |
| 流程與互動設計 | 以 **2 張 Activity Diagram 與 2 張 Sequence Diagram** 呈現兩條端到端流程，涵蓋並行作業、決策、例外與恢復路徑 | [UML 圖表](docs/model-gallery.md) |
| 領域與生命週期設計 | **11 個領域類別、11 個 Animal 持續狀態**，把資料需求連結到允許的業務狀態轉換 | [Class 與 State Machine](docs/model-gallery.md) |
| 整合設計文件 | 完成 **7 張 UML 圖**，涵蓋系統範圍、流程、互動、生命週期與資料結構，並建立功能需求到主要模型的追蹤 | [需求追蹤](docs/traceability.md) |
| 模型驗證紀錄 | EA 完整性檢查顯示 No problems found；相符模型副本的 UML 檢查記錄為 **0 errors、0 warnings** | [驗證結果與範圍](docs/evidence/README.md) |

這份設計將「公開上架資格」、「完成領養」及「實際離所」拆成可檢查的業務決策，並把前置條件、資料欄位與失敗處理寫入需求及模型。[個案與設計成果](docs/case-study.md)進一步說明這些成果如何回應收容所的業務問題。

## 分析方法與技術證據

| 分析方法 | 在完成設計中的應用 | 成果證據 |
| --- | --- | --- |
| 業務需求分析 | 把案例敘述轉成角色、目標、必填資料、前置條件、例外處理與驗收規則 | 7 則功能、7 則非功能故事；[84 項 AC](analysis/acceptance-criteria.csv) |
| 利害關係人與系統範圍分析 | 區分收容所人員、獸醫、地方政府人員、領養者及外部登記系統的責任 | [業務範圍與 Use Case](docs/business-case.md) |
| 流程建模 | 呈現並行評估、合流、留置、治療重檢與申請失敗後的恢復路徑 | [兩張 Activity Diagram](docs/model-gallery.md#activity-diagrams) |
| 系統行為設計 | 將流程轉成訊息互動、回傳資料與持續狀態的轉換 | [Sequence 與 State Machine](docs/model-gallery.md) |
| 物件導向分析 | 定義 11 個領域類別的屬性、操作、關係與多重性 | [Class Diagram](docs/model-gallery.md#class-diagram) |
| 品質需求與追蹤 | 提出權限、隱私、效能、復原、易用性、完整性與無障礙的可測試條件 | [需求追蹤](docs/traceability.md) |
| 模型檢閱與專業溝通 | 對照需求與圖表，修正規則不一致，保存原生工具驗證證據 | [設計理由](docs/design-decisions.md)、[驗證紀錄](docs/evidence/README.md) |

## 三個核心設計判斷

**「完成評估」與「通過資格」分開。** 健康、所有權、行為評估可以並行，但合流只表示各項工作完成。仍在治療、留置未結束或行為不適合，都必須阻擋公開上架。

**「完成領養」與「實際離所」分開。** 簽約及付款確認後才建立領養紀錄；離所前仍須通過最新健康檢查。若出現健康問題，保留領養關係並進入 `Release Paused`，直到治療與重檢通過。

**需求包含失敗與恢復路徑。** 資料不完整要補件、配對不成功要恢復可領養狀態、重複送出完成領養要求不得建立重複紀錄。規則可沿著 AC、流程、狀態與資料模型查閱。

## 我的責任與證據範圍

我負責本專案的需求分析、使用者故事、驗收條件、UML 建模、系統設計決策與報告製作。原始課程報告保留雙人署名；個人工作範圍及修訂版使用 ChatGPT／Codex 輔助的情形，記錄於[貢獻與作者說明](docs/my-contribution.md)。

本庫提供七張 EA 原生完整圖及 12 張放大閱讀圖。提供的驗證紀錄顯示：Report Only 檢查為 **No problems found**；與交付模型記錄雜湊相符的驗證副本，UML 檢查為 **0 errors、0 warnings**。這些工具結果有其範圍；不能延伸為已實作、已通過使用者驗收、取得特定成績或已改善營運成效。

效能、可用性及復原數值均為待確認的設計目標。可用 `python3 scripts/verify_portfolio.py` 重查公開檔案完整性與需求索引；此檢查不會重新執行 EA。

**專案背景：** UQ BISM7255 學術案例，修訂資料日期為 2026 年 10 月 27–28 日。公開庫提供個案分析、設計成果、需求及圖表；完整報告、可編輯 EA 模型與作業題目保存在私人封存庫。[個案與設計成果](docs/case-study.md) · [來源與使用說明](NOTICE.md)。
