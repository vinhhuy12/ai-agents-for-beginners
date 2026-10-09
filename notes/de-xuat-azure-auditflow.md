# Đề xuất: Đưa AuditFlow lên Azure thay vì mở dự án Azure riêng

> Trạng thái: **NHÁP — chưa chốt, chưa thay đổi gì trong Notion.** Huy review trên VSCode trước khi quyết.
> Ngày: 09/10/2026

## Bối cảnh (từ Notion "AuditFlow — Sổ tay dự án")
- Lịch quá tải: ~207h việc vs quỹ ~195h (>15h/tuần). M01–M04 đang "Hoãn", B00–B19 đều "Chưa học". Thi cuối kỳ 24/11–05/12.
- Quyết định "AI-102 → Dời sang 2027" (01/10/2026). AI-102 đã retire 30/06/2026 → mục tiêu thay bằng AI-103 (Developing AI Apps and Agents on Azure).
- Đã có sẵn tín hiệu senior: kiểm mù held-out, đáp án ghi trước, pass^3, Pareto độ đúng × chi phí, trần USD, công bố cả số xấu.
- Tài khoản: Azure for Students (~100 USD credit), đã có Foundry resource (Japan East) + deployment gpt-5-mini GlobalStandard.

## Đề xuất: gắn Azure vào mốc sẵn có
| Mốc/bài | Làm trên Azure | Giá trị CV / AI-103 |
|---|---|---|
| providers/openai.py | Thêm provider Azure OpenAI/Foundry, auth Entra (không key) | ~2–3h, việc đầu tiên |
| M04 VLM người đọc thứ hai | So OCR hiện tại vs Azure Document Intelligence / Content Understanding (gói free giới hạn trang) | Bảng độ đúng × USD/file |
| M09 / B15 RAG pháp lý | pgvector vs Azure AI Search Free (hybrid + semantic ranker), cùng bộ câu hỏi, recall@k + citation accuracy | Trade-off có số liệu |
| M08 hạ tầng demo | Docker → Container Apps, Postgres Flexible, Key Vault, Managed Identity | Enterprise security |
| B09 observability | Giữ Langfuse + OpenTelemetry → App Insights | Biết 2 hệ sinh thái |
| B02 đánh giá | Eval của Huy là chính, chạy thêm Foundry evaluators để so | Phần nặng điểm AI-103 |

## Khoá ai-agents-for-beginners: chỉ học bài khớp
05 Agentic RAG ↔ B15 · 06 Trustworthy ↔ B14 · 08 Multi-agent ↔ B11 · 10 Production ↔ B09 · 11 Protocols ↔ B16 (MCP) · 12 Context engineering ↔ B06 · 13 Memory ↔ B17

## Thời điểm
- Nay → 14/11: chỉ chạy Bài 01 + thêm provider Azure; không lấy giờ đồ án CS2203/CS2229.
- P09 (14–16/11): đưa phương án Azure vào lúc xếp lại M01–M10.
- Sau 06/12: M08 + M09 (vốn ở T12) làm thẳng trên Azure.
- Quý 1/2027: thi AI-103, sau demo HR.

## Dòng CV mẫu (thay số đo thật)
> AuditFlow: agent kiểm toán BCTC trên Azure (Foundry, Document Intelligence, AI Search, Container Apps, Managed Identity). Held-out blind eval, pass^3, đo Pareto độ đúng × chi phí; so sánh pgvector vs Azure AI Search về recall@k/citation accuracy.

## Việc dự kiến trong Notion (CHƯA LÀM)
- Cập nhật trang ⚖️ Quyết định "AI-102" → AI-103.
- Thêm việc Azure vào ✅ Việc cho mốc P09.

---

## Ghi chú review
<!-- Reviewer chỉ THÊM ghi chú dưới đây, không sửa nội dung phía trên. -->

_Reviewer độc lập, 09/10/2026. Đã kiểm chứng bằng web; giá/quota Azure thay đổi thường xuyên, cần soát lại trên portal trước khi tạo tài nguyên._

### 1. Kiểm chứng khẳng định thực tế

- **[Gợi ý]** Bối cảnh, dòng "AI-102 đã retire 30/06/2026 → AI-103": **đúng**. Theo nhiều nguồn thứ cấp, AI-102 và bài gia hạn đều kết thúc ngày 30/06/2026. Trang chứng chỉ chính thức "Azure AI Apps and Agents Developer Associate" đã cho đặt lịch thi AI-103 (120 phút) và không ghi beta. Study guide (skills as of 16/04/2026) có 5 domain: Plan & manage 25–30% · GenAI & agentic 30–35% · Computer vision 10–15% · Text analysis (gồm speech) 10–15% · Information extraction 10–15%. Hệ quả: khoảng 25–40% đề thi (vision/sinh ảnh-video, speech, translator) **không** dự án AuditFlow nào phủ, nên vẫn phải học riêng. Quyết định "AI-102 → dời 2027" trong Notion đã mất đối tượng, cần đổi hẳn thành AI-103 chứ không phải "dời". Nguồn: [Chứng chỉ AI-103](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-103/), [Study guide AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [certcrush: AI-102 vs AI-103](https://www.certcrush.app/blog/ai-102-vs-ai-103-which-azure-ai-cert-2026).
- **[Nghiêm trọng]** Dòng M04, cụm "gói free giới hạn trang": Document Intelligence F0 **chỉ phân tích 2 trang đầu mỗi request, file tối đa 4 MB, 1 TPS**. Một BCTC thường dài 20–60 trang PDF scan, nên F0 không đo được độ đúng trên trọn file. Muốn có "bảng độ đúng × USD/file" thì phải dùng S0 (trả theo trang) hoặc tự cắt file thành từng request 2 trang. Cách cắt file làm sai lệch số đo về layout/bảng vắt trang. Hạn mức "500 trang/tháng" chỉ thấy ở nguồn thứ ba, chưa xác nhận. Content Understanding đã GA (API 2025-11-01) nhưng **không có gói free**: tính theo trang, cộng thêm token của model sinh khi trích field. Nguồn: [DI service limits](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/service-limits), [CU pricing explainer](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/pricing-explainer).
- **[Nên sửa]** Dòng M09/B15, cụm "AI Search Free (hybrid + semantic ranker)": gói Free cho **50 MB tổng (tính cả vector), 3 index, 3 indexer**, không có SLA, hạ tầng dùng chung, mỗi subscription chỉ được 1 service, và **có thể bị xoá nếu không dùng lâu**. Với embedding 1536 chiều kiểu float32 (khoảng 6 KB/chunk), trần thực tế chỉ vài nghìn chunk, nên corpus pháp lý (VAS, Thông tư 200, Luật Kiểm toán…) có thể không vừa nếu không nén/giảm chiều. Về semantic ranker ở gói Free, tài liệu Microsoft **mâu thuẫn nhau**: bảng tier ghi "không có", trang overview ghi "dùng free trong giới hạn gói Free". Phải tự thử trước khi đưa vào thiết kế thí nghiệm. Nguồn: [Search service limits](https://learn.microsoft.com/azure/search/search-limits-quotas-capacity), [Semantic ranking overview](https://learn.microsoft.com/azure/search/semantic-search-overview), [Choose a tier](https://learn.microsoft.com/azure/search/search-sku-tier).
- **[Nên sửa]** Dòng M08, cụm "Postgres Flexible": Azure for Students có 750 giờ B1MS, 32 GB storage và 32 GB backup mỗi tháng, nhưng **chỉ trong 12 tháng đầu và chỉ cho khách hàng mới**. Cần kiểm tra ngày tạo tài khoản: nếu tạo từ 10/2025 trở về trước thì đến T12/2026 đã hết hạn mức free, và mức giá B1MS sẽ trừ vào 100 USD. Chỉ được free với đúng 1 instance B1MS: bật HA, chọn tier khác hoặc tăng storage là bị tính tiền. Nguồn: [Azure for Students](https://azure.microsoft.com/en-us/free/students), [Free services](https://azure.microsoft.com/pricing/free-services/).
- **[Gợi ý]** pgvector **chạy được** trên Postgres Flexible: thêm `vector` vào allowlist `azure.extensions`, rồi `CREATE EXTENSION vector;` ở từng DB. Nguồn: [How to use pgvector](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector).
- **[Gợi ý]** Container Apps free grant: 180.000 vCPU-s, 360.000 GiB-s và 2 triệu request mỗi tháng, tính trên subscription. Chỉ an toàn nếu để scale-to-zero (`minReplicas=0`); đặt min = 1 thì 1 replica 0,5 vCPU chạy 24/7 tốn khoảng 1,3 triệu vCPU-s/tháng, gấp khoảng 7 lần grant. Nguồn: [Container Apps pricing](https://azure.microsoft.com/en-ca/pricing/details/container-apps/).

### 2. Quỹ giờ: "không tốn thêm giờ" là không đúng

- **[Nghiêm trọng]** Phần "Thời điểm" và bảng đề xuất: đề xuất không ghi đủ chi phí giờ. Ước lượng giờ **thêm** so với làm cùng mốc đó mà không dùng Azure, cho người lần đầu làm Azure:
  - providers Azure + Entra: **4–6h**, không phải 2–3h. Phần việc gồm RBAC "Cognitive Services OpenAI User", `DefaultAzureCredential` chạy được cả local lẫn CI, khác biệt tham số của gpt-5-mini, xử lý quota/429 và test.
  - M04 DI/CU: **8–12h**, gồm cắt trang hoặc mở S0, chuẩn hoá output về schema hiện có, chấm trên bộ có nhãn. Nếu làm cả CU thì cộng thêm 4–6h.
  - M09 pgvector vs AI Search: **10–15h**, gồm schema index, analyzer tiếng Việt, đẩy chunk sao cho giống hệt cách chunk của pgvector, chạy lại bộ câu hỏi, xử lý trần 50 MB.
  - M08 hạ tầng: **12–20h**, gồm ACR, Container Apps env, Managed Identity → Postgres (Entra auth) + Key Vault, networking/firewall, debug lần deploy đầu.
  - B09 App Insights: **3–5h**. B02 Foundry evaluators: **4–6h**.
  - **Tổng khoảng 41–64h**, chưa tính việc học AI-103. Với ~207h việc / ~195h quỹ thì tổng thành khoảng 250–270h, tức quá tải 28–38%. Ghi "không lấy giờ đồ án" mà không chỉ ra giờ lấy từ đâu thì chỉ là mong muốn, chưa phải kế hoạch.
- **[Nên sửa]** Phần "Nay → 14/11": provider Azure, dù nhỏ, vẫn rơi vào 5 tuần trước kỳ thi 24/11–05/12 trong khi M01–M04 đang "Hoãn". Đề nghị trước 14/11 **chỉ làm provider** (giới hạn 6h) và bỏ "Bài 01". Mọi việc còn lại đưa vào P09 như một **phương án thay thế** việc cũ (không cộng dồn), kèm danh sách việc bị cắt tương ứng.

### 3. Chi phí so với 100 USD

- **[Nên sửa]** Toàn bảng: đề xuất không có dòng chi phí nào. Các chi phí ẩn chính:
  - **ACR Basic** khoảng 5 USD/tháng, không có free. Có thể dùng GHCR để né.
  - **Log Analytics/App Insights** tính theo GB ingest khi vượt mức free. Trace LLM kèm prompt/completion rất nặng.
  - **AI Search**: nếu vượt 50 MB và "nâng tạm" lên Basic thì khoảng 70+ USD/tháng, đủ cạn credit trong khoảng 1 tháng.
  - **Postgres** khi hết 12 tháng free.
  - **DI S0 / CU** tính theo trang. **Foundry evaluators** dùng LLM-as-judge nên tốn token. **Embedding** để index hai lần (pgvector và AI Search).
  - Khi hết credit, subscription Students bị **vô hiệu hoá**, có rủi ro mất DB/index nếu không backup.
- Đề nghị: đặt **Budget alert** ở 25/50/75 USD, tag mọi tài nguyên, viết script `down` (xoá resource group) và ghi trần USD theo từng thí nghiệm. Cách này khớp với tín hiệu "trần USD" mà Huy đã có.

### 4. Phần nên cắt / phần còn thiếu

- **[Nên sửa]** Cắt bớt: (a) **Content Understanding**: chỉ giữ DI Layout làm "người đọc thứ hai", CU để sau. (b) **Foundry evaluators**: biên lợi ích thấp vì eval của Huy đã mạnh hơn. Chỉ chạy 1 lần để biết dùng, không đưa vào số liệu chính. (c) **Key Vault**: nếu mọi kết nối đã dùng Managed Identity thì Key Vault gần như trống. Giữ lại chỉ khi thật sự có secret bên thứ ba (Langfuse key).
- **[Nên sửa]** Thiếu **IaC (Bicep hoặc `azd`)** và **CI/CD (GitHub Actions + OIDC federated credential, không lưu secret)**. AI-103 có hẳn mục "Integrate Foundry projects with CI/CD pipelines". Với CV mid/senior, "tạo bằng portal" ít giá trị hơn "`azd up` dựng lại toàn bộ trong N phút". IaC còn giúp xoá/dựng lại tài nguyên để giữ chi phí.
- **[Nên sửa]** Thiếu **Responsible AI**. Domain Plan & manage (25–30%) có content filter, prompt shields/indirect prompt injection, groundedness, audit trail. Với BCTC (PDF scan có thể chứa chỉ dẫn độc hại, dẫn đến prompt injection), bài 06 Trustworthy ↔ B14 nên có ít nhất 1 thí nghiệm prompt shields/groundedness có số đo.
- **[Nghiêm trọng]** Thiếu **data residency & bảo mật dữ liệu BCTC khách hàng**. Deployment **GlobalStandard** có thể xử lý suy luận ở bất kỳ region nào; Foundry hiện đặt ở Japan East. BCTC chưa công bố của khách hàng thuộc nghĩa vụ bảo mật nghề nghiệp kiểm toán. Nếu BCTC có dữ liệu cá nhân (thuyết minh bên liên quan, lương ban điều hành) thì còn chịu **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 (hiệu lực 01/01/2026)**, với yêu cầu đánh giá tác động khi chuyển dữ liệu ra nước ngoài. Đề nghị ghi rõ: chỉ dùng BCTC **đã công bố** (doanh nghiệp niêm yết) hoặc dữ liệu tổng hợp/ẩn danh. Nếu buộc phải dùng dữ liệu thật thì cân nhắc DataZone/Standard deployment và ghi chính sách lưu trữ/xoá. Nguồn: [Tilleke – Vietnam PDPL](https://www.tilleke.com/insights/vietnam-issues-personal-data-protection-law), [EY legal alert 07/2025](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-vn/technical/tax/documents/legal-alert-july-2025-personal-data-protection-law-en.pdf).
- **[Nên sửa]** **Vendor lock-in cho luận văn**: khi credit hết, hội đồng hay chính Huy sẽ không chạy lại được thí nghiệm, nên không tái lập được. Semantic ranker và Foundry evaluators là hộp đen, phiên bản có thể đổi mà không báo. Đề nghị: giữ **pgvector + eval riêng làm đường chính**, Azure chỉ là nhánh so sánh qua lớp `providers/`; cache toàn bộ output thô; ghi API version/model version; kết quả cốt lõi của luận văn không được phụ thuộc vào dịch vụ trả phí.

### 5. Dòng CV mẫu

- **[Nên sửa]** Có dấu hiệu phóng đại/nhồi keyword:
  - "agent kiểm toán BCTC **trên Azure**" kèm danh sách 5 dịch vụ trong khi DI chỉ chạy F0 2 trang/request, AI Search ở gói Free 50 MB, demo scale-to-zero. Interviewer senior sẽ hỏi sâu từng dịch vụ.
  - "kiểm toán" nên viết là "hỗ trợ rà soát BCTC", vì kiểm toán là hoạt động hành nghề có điều kiện.
  - Đề nghị: chỉ liệt kê dịch vụ đã chạy thật kèm quy mô (số BCTC, số câu hỏi, chi phí/tháng), đặt con số kết quả lên đầu. Ví dụ: "recall@5 X% vs Y%, chi phí Z USD/1.000 trang; dựng bằng Bicep/azd, CI/CD OIDC, không secret". Bỏ những dịch vụ mới chỉ "đã thử".

### Kết luận reviewer

Hướng "gắn Azure vào mốc sẵn có" là đúng và tốt hơn mở dự án riêng, nhưng khẳng định "không tốn thêm giờ" là **sai**: ước tính thêm khoảng 41–64h trên một lịch đã quá tải. Gói free cũng hẹp hơn đề xuất ngầm định (DI F0 2 trang/request, AI Search Free 50 MB, semantic ranker free chưa chắc, CU không free, Postgres free chỉ 12 tháng đầu).
Trước khi chốt ở P09: (1) cắt CU, Foundry evaluators và Key Vault; (2) thêm Bicep/azd + CI/CD OIDC + budget alert; (3) viết rõ chính sách dữ liệu, chỉ dùng BCTC đã công bố; (4) giữ pgvector/eval riêng làm đường chính để luận văn tái lập được; (5) mỗi việc Azure phải **thay** một việc cũ, không cộng dồn.
Trước 24/11 chỉ làm provider Azure (≤6h).
