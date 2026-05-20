from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": _("Portfolio Admin"),
    "SITE_HEADER": _("Portfolio"),
    "SITE_URL": "/",
    "SITE_SYMBOL": "speed",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "DASHBOARD_CALLBACK": "core.unfold_callbacks.dashboard_callback",
    "STYLES": [
        lambda request: static("admin_custom.css"),
    ],
    "SCRIPTS": [
        lambda request: static("admin_custom.js"),
    ],
    "COLORS": {
        "primary": {
            "50": "240 253 250",
            "100": "204 251 241",
            "200": "153 246 228",
            "300": "94 234 212",
            "400": "45 212 191",
            "500": "20 184 166",
            "600": "13 148 136",
            "700": "15 118 110",
            "800": "17 94 89",
            "900": "19 78 74",
            "950": "4 47 46",
        },
    },
    "LOGIN": {
        "image": None,
        "form": "core.forms.CustomAdminAuthenticationForm",
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": _("Overview"),
                "separator": True,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                ],
            },
            {
                "title": _("Main Content"),
                "separator": True,
                "items": [
                    {
                        "title": _("Profiles"),
                        "icon": "person",
                        "link": reverse_lazy("admin:main_profile_changelist"),
                    },
                    {
                        "title": _("Services"),
                        "icon": "design_services",
                        "link": reverse_lazy("admin:main_service_changelist"),
                    },
                    {
                        "title": _("Testimonials"),
                        "icon": "reviews",
                        "link": reverse_lazy("admin:main_testimonial_changelist"),
                    },
                    {
                        "title": _("Messages"),
                        "icon": "mail",
                        "link": reverse_lazy("admin:main_contactmessage_changelist"),
                    },
                ],
            },
            {
                "title": _("Resume & Skills"),
                "separator": True,
                "items": [
                    {
                        "title": _("Experiences"),
                        "icon": "work",
                        "link": reverse_lazy("admin:resume_experience_changelist"),
                    },
                    {
                        "title": _("Educations"),
                        "icon": "school",
                        "link": reverse_lazy("admin:resume_education_changelist"),
                    },
                    {
                        "title": _("Skills"),
                        "icon": "psychology",
                        "link": reverse_lazy("admin:resume_skill_changelist"),
                    },
                ],
            },
            {
                "title": _("Projects"),
                "separator": True,
                "items": [
                    {
                        "title": _("Projects"),
                        "icon": "business_center",
                        "link": reverse_lazy("admin:project_project_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:project_category_changelist"),
                    },
                ],
            },
            {
                "title": _("Blog"),
                "separator": True,
                "items": [
                    {
                        "title": _("Posts"),
                        "icon": "article",
                        "link": reverse_lazy("admin:blog_post_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "label",
                        "link": reverse_lazy("admin:blog_category_changelist"),
                    },
                ],
            },
            {
                "title": _("AI Job Manager"),
                "separator": True,
                "items": [
                    {
                        "title": _("Applications"),
                        "icon": "smart_toy",
                        "link": reverse_lazy("admin:job_manager_jobapplication_changelist"),
                    },
                ],
            },
        ],
    },
}
