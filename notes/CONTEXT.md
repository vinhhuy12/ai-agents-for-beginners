# Ngữ cảnh làm việc (bàn giao từ phiên Claude Code trên cloud)

> File này để Claude Code (VSCode/CLI) đọc khi mở repo. Cập nhật lần cuối: 11/10/2026.
> Đây là **ngữ cảnh**, không phải quyết định đã chốt. Mọi thay đổi Notion/Azure đều phải hỏi Huy trước.

## Người dùng
- Huy: AI engineer, đang học thạc sĩ (CS2203, CS2229), muốn lên mid/senior AI engineer và ghi Azure vào CV.
- Trả lời bằng **tiếng Việt**.
- Thích review trước khi chốt: khi được nhờ review thì **chỉ thêm ghi chú, không sửa/thay nội dung gốc**.

## Ba thứ tách biệt — đừng trộn
1. **Khoá ai-agents-for-beginners (repo này):** đang học từng bài. Đây là việc chính hiện tại.
2. **AuditFlow** (dự án riêng, repo khác): agent kiểm tra BCTC. Kế hoạch, mốc M00–M10, bài học B00–B19 nằm trong Notion "AuditFlow — Sổ tay dự án".
3. **Luận văn / báo cáo khoa học:** KHÁC AuditFlow. Chỉ trùng phần **đánh giá**: đánh giá LLM, đánh giá ảnh (VLM), đánh giá agent, đánh giá harness. Các phần khác của luận văn: không cần làm, không cần đề xuất.

## Môi trường Azure
- Subscription: Azure for Students (~100 USD credit, hết credit thì dừng, không tự trừ tiền).
- Có 1 Foundry resource (Japan East, S0) + 1 project; model deployment `gpt-5-mini` (GlobalStandard, trả theo token, không có phí cố định).
- Biến môi trường: `AZURE_AI_PROJECT_ENDPOINT`, `AZURE_AI_MODEL_DEPLOYMENT_NAME`. Đăng nhập: `az login --use-device-code`, code dùng `AzureCliCredential`.
- Cẩn thận chi phí: AI Search chọn gói Free; không tạo VM/AKS/Provisioned Throughput; nên đặt budget alert.

## Lỗi quan trọng của repo: API đã đổi
- `agent-framework` 1.21 **đã bỏ** `agent_framework.azure.AzureAIProjectAgentProvider`. 14/17 notebook trong `*/code_samples/` dùng tên này nên sẽ lỗi `ImportError`.
- API mới chạy được (đã thử thật ngày 10/10/2026, xem `notes/lesson01_foundry_api.py`):
  ```python
  from agent_framework import Agent, tool
  from agent_framework.foundry import FoundryChatClient
  client = FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())
  agent = Agent(client=client, name=..., instructions=..., tools=[...])
  await agent.run("...")              # hoặc stream=True
  ```
- Còn có `FoundryAgent` (gắn với agent đã đăng ký sẵn trên Foundry), `FoundryEvals`, `evaluate_traces`, `FoundryMemoryProvider` trong `agent_framework_foundry`.
- **Chưa chốt** cách học các bài sau: (A) viết bản chạy được bằng API mới vào thư mục `hoc/`, giữ notebook gốc — đang khuyến nghị; hoặc (B) cài agent-framework bản cũ để chạy notebook nguyên văn.

## Tiến độ học
- Bài 01: đã chạy xong (bản API mới). Rút ra: vòng lặp agent; `@tool` biến docstring + type hint thành schema; agent **gọi tool thừa** với câu hỏi "Tokyo" (→ ví dụ cho đánh giá quỹ đạo/trajectory, không chỉ chấm output); gpt-5-mini tốn reasoning token (384/925 token output).
- Bài tập Bài 01 đang mở: (1) chạy câu Tokyo 5 lần, đếm tỉ lệ gọi tool thừa; (2) sửa docstring rồi đo lại (A/B); (3) thêm tool giả `get_weather(city)`.
- Bài tiếp theo: Bài 02.
- Bài nên nhấn mạnh vì gắn với đánh giá / AuditFlow: 05 Agentic RAG ↔ B15, 06 Trustworthy ↔ B14, 08 Multi-agent ↔ B11, 10 Production ↔ B09, 11 Protocols/MCP ↔ B16, 12 Context engineering ↔ B06, 13 Memory ↔ B17.

## Hướng nghề / chứng chỉ (đã nghiên cứu)
- AI-102 đã retire 30/06/2026 → mục tiêu thay bằng **AI-103** (Developing AI Apps and Agents on Azure). Trong Notion, quyết định "AI-102: dời sang 2027" chưa được cập nhật.
- Đề xuất "đưa AuditFlow lên Azure" + ghi chú review của agent: `notes/de-xuat-azure-auditflow.md` — **nháp, Huy chưa chốt**. Review chỉ ra: tốn thêm ~41–64h (lịch đã quá tải), Document Intelligence F0 chỉ đọc 2 trang/request, lưu ý dữ liệu BCTC khách hàng (chỉ dùng BCTC đã công bố).
