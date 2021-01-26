from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Tuple

from dataclasses_json import dataclass_json
####################### Response ###############################################


@dataclass_json
@dataclass(frozen=True)
class Response:
    landing_id: str
    token: str
    response_id: str
    landed_at: datetime
    submitted_at: datetime

    @dataclass_json
    @dataclass(frozen=True)
    class Metadata:
        user_agent: str
        platform: str
        referer: str
        network_id: str
        browser: str

    metadata: Metadata
    hidden: Dict

    @dataclass_json
    @dataclass(frozen=True)
    class Definition:
        @dataclass_json
        @dataclass(frozen=True)
        class PartialDef:
            id: str
            type: str
            title: str
            description: str
        
        fields: List[PartialDef]
    definition: Definition

    @dataclass_json
    @dataclass(frozen=True)
    class Answer:
        @dataclass_json
        @dataclass(frozen=True)
        class Field:
            id: str
            type: str
            ref: str
            title: str

        field: Field
        #TODO: Replace functional Enum constructors with class derived from Enum
        @dataclass_json
        @dataclass(frozen=True)
        class AnswerType(Enum):
            choice = 'choice'
            choices = 'choices'
            date = 'date'
            email = 'email'
            url = 'url'
            file_url = 'file_url'
            number = 'number'
            boolean = 'boolean'
            text = 'text'
            payment = 'payment'
        )
        type: AnswerType

        @dataclass_json
        @dataclass(frozen=True)
        class Choice:
            label: str
            other: str

        choice: Choice

        @dataclass_json
        @dataclass(frozen=True)
        class Choices:
            labels: List[str]
            other: str

        choices: Choices
        date: str
        email: str
        file_url: str
        number: float
        boolean: bool
        text: str
        url: str

        @dataclass_json
        @dataclass(frozen=True)
        class Payment:
            amount: str
            last4: str
            name: str

        payment: Payment
        
        @dataclass_json
        @dataclass(frozen=True)
        class Calculated:
            score: float
        calculated: Calculated

        

    answers: List[Answer]

    @dataclass_json
    @dataclass(frozen=True)
    class Calculated:
        score: float

    calculated: Calculated


###########################   Form classes #####################################

@dataclass_json
@dataclass(frozen=True)
class Form:
    id: str
    title: str

    @dataclass_json
    @dataclass(frozen=True)
    class Field:
        FieldType = dataclass_json(dataclass(Enum(
            "FieldType",
            [
                "ranking",
                "date",
                "dropdown",
                "email",
                "file_upload",
                "group",
                "legal",
                "long_text",
                "multiple_choice",
                "number",
                "opinion_scale",
                "payment",
                "picture_choice",
                "rating",
                "short_text",
                "statement",
                "website",
                "yes_no",
                "phone_number",
            ],
        )))
        id: str
        ref: str
        title: str
        type: FieldType

    fields: List[Field]
    hidden: List[str]
    
    @dataclass_json
    @dataclass(frozen=True)
    class WelcomeScreen:
        ref: str
        title: str

        @dataclass_json
        @dataclass(frozen=True)
        class Properties:
            description: str
            show_button: bool
            button_text: str

        properties: Properties

        @dataclass_json
        @dataclass(frozen=True)
        class Attachment:
            AttachmentType = Enum(
                "AttachmentType",
                [
                    "image",
                    "video",
                ],
            )
            type: AttachmentType
            href: str
            scale: float
            
            @dataclass_json
            @dataclass(frozen=True)
            class Properties:
                description: str

            properties: Properties

        attachment: Attachment

        @dataclass_json
        @dataclass(frozen=True)
        class Layout:
            LayoutType = Enum("LayoutType", ["split", "wallpaper", "float"])
            type: LayoutType
            LayoutPlacement = Enum("LayoutPlacement", ["left", "right"])
            placement: LayoutPlacement

            @dataclass_json
            @dataclass(frozen=True)
            class Attachment:
                type: str
                href: str
                scale: float

                @dataclass_json
                @dataclass(frozen=True)
                class Properties:
                    brightness: float
                    description: str

                    @dataclass_json
                    @dataclass(frozen=True)
                    class FocalPoint:
                        x: float
                        y: float

                properties: Properties

            attachment: Attachment

        layout: Layout

    welcome_screens: List[WelcomeScreen]

    @dataclass_json
    @dataclass(frozen=True)
    class ThankyouScreen:
        ref: str
        title: str

        @dataclass_json
        @dataclass(frozen=True)
        class Properties:  # ThankyouScreen.Properties
            show_button: bool
            button_text: str
            button_mode: str
            redirect_url: str
            share_icons: bool

        properties: Properties

        @dataclass_json
        @dataclass(frozen=True)
        class Attachment:  # ThankyouScreen.Attachment
            AttachmentType = Enum("AttachmentType", ["image", "video"])
            type: AttachmentType
            href: str
            scale: float

            @dataclass_json
            @dataclass(frozen=True)
            class Properties:
                description: str

            properties: Properties

        attachment: Attachment

    @dataclass_json
    @dataclass(frozen=True)
    class Layout:  # ThankyouScreen.Layout
        LayoutType = Enum("LayoutType", ["split", "wallpaper", "float"])
        type: LayoutType
        LayoutPlacement = Enum("LayoutPlacement", ["left", "right"])
        placement: LayoutPlacement

        @dataclass_json
        @dataclass(frozen=True)
        class Attachment:
            AttachmentType = Enum("AttachmentType", ["image", "video"])
            type: AttachmentType
            href: str
            scale: float

            @dataclass_json
            @dataclass(frozen=True)
            class Properties:
                brightness: float
                description: str

                @dataclass_json
                @dataclass(frozen=True)
                class FocalPoint:
                    x: float
                    y: float

            properties: Properties

        attachment: Attachment

    layout: Layout
    thankyou_screens: List[ThankyouScreen]

    @dataclass_json
    @dataclass(frozen=True)
    class Logic:
        type: str
        ref: str

        @dataclass_json
        @dataclass(frozen=True)
        class Action:
            ActionsEnum = Enum(
            "ActionsEnum", ["jump", "add", "subtract", "multiply", "divide"]
        )

            action: ActionsEnum

            @dataclass_json
            @dataclass(frozen=True)
            class Details:

                @dataclass_json
                @dataclass(frozen=True)
                class To:
                    type: str
                    value: str

                to: To

                @dataclass_json
                @dataclass(frozen=True)
                class Target:
                    type: str
                    value: str

                target: Target

                @dataclass_json
                @dataclass(frozen=True)
                class Value:
                    type: str
                    value: str

                value: Value

            details: Details

            @dataclass_json
            @dataclass(frozen=True)
            class Condition:
                Op = Enum(
                "Op",
                [
                "begins_with",
                "ends_with",
                "contains",
                "not_contains",
                "lower_than",
                "lower_equal_than",
                "greater_than",
                "greater_equal_than",
                "is",
                "is_not",
                "equal",
                "not_equal",
                "always",
                "on",
                "not_on",
                "earlier_than",
                "earlier_than_or_on",
                "later_than",
                "later_than_or_on",
                ],
                )
                op: Op

                @dataclass_json
                @dataclass(frozen=True)
                class Vars:
                    VarsType = Enum(
                    "VarsType",
                    [
                    "field",
                    "hidden",
                    "variable",
                    "constant",
                    "end",
                    ],
                    )
                    type: VarsType
                    value: Dict

                vars: Vars
            condition: Condition

        actions: List[Action]

    logic: List[Logic]

    @dataclass_json
    @dataclass(frozen=True)
    class Theme:
        href: str

    theme: Theme
    
    @dataclass_json
    @dataclass(frozen=True)
    class Workspace:
        href: str

    workspace: Workspace

    @dataclass_json
    @dataclass(frozen=True)
    class _Links:
        display: str

    _links: List[_Links]

    @dataclass_json
    @dataclass(frozen=True)
    class Settings:
        Language = Enum(
            "Language",
            [
                "en",
                "es",
                "ca",
                "fr",
                "de",
                "ru",
                "it",
                "da",
                "pt",
                "ch",
                "zh",
                "nl",
                "no",
                "uk",
                "ja",
                "ko",
                "hr",
                "fi",
                "sv",
                "pl",
                "el",
                "hu",
                "tr",
                "cs",
                "et",
                "di",
            ],
        )
        language: Language
        is_public: bool
        progress_bar: str
        show_progress_bar: bool
        show_typeform_branding: bool
        show_time_to_complete: bool
        hide_navigation: bool

        @dataclass_json
        @dataclass(frozen=True)
        class Meta:
            title: str
            allow_indexing: bool
            description: str
            
            @dataclass_json
            @dataclass(frozen=True)
            class Image:
                href: str

            image: Image

        meta: Meta
        redirect_after_submit_url: str
        google_analytics: str
        facebook_pixel: str
        google_tag_manager: str

        @dataclass_json
        @dataclass(frozen=True)
        class Notifications:
            class SelfNotification:
                enabled: bool
                recipients: List[str]
                reply_to: str
                subject: str
                message: str

            selfnotification: SelfNotification

            @dataclass_json
            @dataclass(frozen=True)
            class Respondent:
                enabled: bool
                recipient: str
                reply_to: List[str]
                subject: str
                message: str

            respondent: Respondent

        notifications: Notifications

    settings: Settings

    @dataclass_json
    @dataclass(frozen=True)
    class CuiSettings:
        avatar: str
        is_typing_emulation_disabled: bool
        SpeedEnum = Enum(
            "SpeedEnum",
            [
                "slow",
                "medium",
                "fast",
            ],
        )
        typing_emulation_speed: SpeedEnum

    cui_settings: CuiSettings
    language: str = "en"