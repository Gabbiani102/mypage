{
    "name": "Livestock ERP - Base Master Data",
    "version": "17.0.1.0.0",
    "summary": "축산물(소/돼지/닭/수입우/수입돈) 유통 ERP 마스터 데이터",
    "description": """
축산물 전문 유통/생산 ERP의 기초 마스터 데이터 모듈.
- 축종(species) / 등급(grade) 마스터
- 거래처 영업채널(B2B/B2C/직영매장/가맹매장/외식사업장) 분류
- 품목(product.template)에 축종/등급/원산지(국내/수입) 확장 필드 추가
- 이후 모듈(축평원 이력연동, 미트와치 연동, MRP 연동 등)이 참조할 기준 데이터 정의
    """,
    "category": "Industries",
    "license": "LGPL-3",
    "depends": ["base", "sale", "stock", "product"],
    "data": [
        "security/ir.model.access.csv",
        "data/livestock_species_data.xml",
        "data/livestock_grade_data.xml",
        "data/livestock_common_code_data.xml",
        "views/livestock_species_views.xml",
        "views/livestock_grade_views.xml",
        "views/common_code_views.xml",
        "views/res_partner_views.xml",
        "views/product_template_views.xml",
        "views/livestock_base_menus.xml",
    ],
    "installable": True,
    "application": True,
}
