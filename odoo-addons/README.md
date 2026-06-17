# Livestock ERP (Odoo 17 CE 기반)

축산물(소/돼지/닭/수입우/수입돈) 유통·생산 ERP를 Odoo 17 Community Edition 위에 구축하는 커스텀 모듈 모음입니다.

## 라이선스/법적 메모
- 기반: Odoo 17 Community Edition (LGPL-3) — 자유 사용/수정 가능
- Enterprise 전용 모듈은 사용하지 않음
- 타사 ERP는 프로세스만 참고하여 직접 설계/구현 (코드 복제 없음)
- 축평원 공공데이터포털 API: 발급받은 키로 이용약관 준수하여 연동
- 미트와치 API: 별도 사업자 제휴/계약 필요 (법무 검토 별도 진행)

## 모듈 로드맵
| 단계 | 모듈 | 상태 |
|---|---|---|
| 1 | `livestock_base` (축종/등급/거래처 채널/품목 확장) | 완료 |
| 2 | `livestock_sale` (B2B/B2C/직영/가맹/외식 채널별 수주 → MRP 트리거) | 예정 |
| 3 | `livestock_mrp_integration` (수주 → 구매요청/작업지시 자동 연동) | 예정 |
| 4 | `livestock_logistics` (거래명세서 기준 배송준비/재고차감) | 예정 |
| 5 | `livestock_traceability` (축평원 이력번호 연동) | 예정 |
| 6 | `meatwatch_integration` (미트와치 API 연동) | 예정 |
| 7 | `livestock_account_fintech` (세금계산서 + 핀테크 회계 연동) | 예정 |

## livestock_base 모듈 구성
- `livestock.species`: 축종 마스터 (소/돼지/닭 국내, 수입우/수입돈)
- `livestock.grade`: 축종별 등급 마스터 (축평원 등급 기준, 시드 데이터 포함)
- `res.partner.sales_channel`: 거래처 영업채널 (B2B/B2C/직영매장/가맹매장/외식사업장)
- `product.template`: 축종/등급/원산지/이력추적 대상 여부 확장 필드

## 설치 방법 (로컬 Docker 환경)
`odoo-docker-compose.yml`의 `./addons` 볼륨 경로를 이 `odoo-addons` 폴더로 매핑한 뒤,
Odoo 실행 시 `--addons-path`에 포함하거나 Apps 메뉴에서 업데이트 후 설치하세요.
