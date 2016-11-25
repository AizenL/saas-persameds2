{
    "name" : "HR Meal Voucher",
    "version" : "1.0",
    "depends" : ["account",
                 "hr",
                 "dos_hr_indonesia",
                 "hr_attendance",
                 "hr_contract",
                 "hr_payroll",
                 "hr_holidays",
                 "dos_hr_holiday_year",
                 "dos_hr_overtime",
                 "dos_hr_bpjs",
                 "dos_leave_management",
                 "report_xls"
                 ],
    "author" : "DATABIT",
    "description": """This module is aimed to handle Employee Payroll in Malinda Furniture Gallery.
    """,
    "website" : "http://www.databit.co.id",
    "category" : "Human Resource Management",
    "init_xml" : [],
    "demo_xml" : [],
    'test': [],
    "update_xml" : [
        "workflow.xml",
        "hr_attendance_summary_view.xml",
        "hr_payroll_view.xml",
        "hr_contract_view.xml",
        "hr_spt_view.xml",
        "substitute_working_schedule_view.xml",
        #"hr_holidays_view.xml",
        "hr_import_attendance_view.xml",
        "hr_absence_view.xml",
        "correction_view.xml",
        "kokara_view.xml",
        "abacus_bhakti_view.xml",
        "hr_benefit_view.xml",
        'wizard/wiz_import_attendance.xml',
        "report/report_view.xml",
        "report/payslip_template.xml",
        "report/payroll_summary_xls.xml",
        "wizard/wizz_payroll_summary.xml",
    ],
    "active": False,
    "installable": True,
}
