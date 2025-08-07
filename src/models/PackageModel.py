
from pydantic import Field, validator
from typing import List, Union, Literal
from sdks.novavision.src.base.model import Package, Input, Output, Image, Config, Inputs, Configs, Outputs, Response, Request, Detection


class ConfigCustomColors(Config):
    """
        List of colors to use for annotations '#FF0000, #00FF00, #0000FF'
    """
    name: Literal["CustomColors"] = "CustomColors"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Custom Colors"


class ColorPaletteCustom(Config):
    name: Literal["ColorPaletteCustom"] = "ColorPaletteCustom"
    configCustomColors: ConfigCustomColors
    value: Literal["custom"] = "custom"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Custom"


class ConfigPaletteSize(Config):
    """
        Number of colors in the color palette. Applies when using a matplotlib `color_palette`.
    """
    name: Literal["ConfigPaletteSize"] = "ConfigPaletteSize"
    value: int = Field(ge=1, le=100)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Color Palette Size"


class ColorPaletteTab20c(Config):
    name: Literal["ColorPaletteTab20c"] = "ColorPaletteTab20c"
    configPaletteSize: ConfigPaletteSize
    value: Literal["tab20c"] = "tab20c"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Tab20c"


class ColorPaletteTab20b(Config):
    name: Literal["ColorPaletteTab20b"] = "ColorPaletteTab20b"
    configPaletteSize: ConfigPaletteSize
    value: Literal["tab20b"] = "tab20b"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Tab20b"


class ColorPaletteTab20(Config):
    name: Literal["ColorPaletteTab20"] = "ColorPaletteTab20"
    configPaletteSize: ConfigPaletteSize
    value: Literal["tab20"] = "tab20"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Tab20"


class ColorPaletteTab10(Config):
    name: Literal["ColorPaletteTab10"] = "ColorPaletteTab10"
    configPaletteSize: ConfigPaletteSize
    value: Literal["tab10"] = "tab10"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Tab10"


class ColorPaletteSet3(Config):
    name: Literal["ColorPaletteSet3"] = "ColorPaletteSet3"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Set3"] = "Set3"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Set3"


class ColorPaletteSet2(Config):
    name: Literal["ColorPaletteSet2"] = "ColorPaletteSet2"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Set2"] = "Set2"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Set2"


class ColorPaletteSet1(Config):
    name: Literal["ColorPaletteSet1"] = "ColorPaletteSet1"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Set1"] = "Set1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Set1"


class ColorPaletteDark2(Config):
    name: Literal["ColorPaletteDark2"] = "ColorPaletteDark2"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Dark2"] = "Dark2"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Dark2"


class ColorPaletteAccent(Config):
    name: Literal["ColorPaletteAccent"] = "ColorPaletteAccent"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Accent"] = "Accent"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Accent"


class ColorPalettePaired(Config):
    name: Literal["ColorPalettePaired"] = "ColorPalettePaired"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Paired"] = "Paired"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Paired"


class ColorPalettePastel2(Config):
    name: Literal["ColorPalettePastel2"] = "ColorPalettePastel2"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Pastel2"] = "Pastel2"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Pastel2"


class ColorPalettePastel1(Config):
    name: Literal["ColorPalettePastel1"] = "ColorPalettePastel1"
    configPaletteSize: ConfigPaletteSize
    value: Literal["Pastel1"] = "Pastel1"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Pastel1"


class ConfigColorPalette(Config):
    """
        Color palette to use for annotations.
    """
    name: Literal["ConfigColorPalette"] = "ConfigColorPalette"
    value: Union[
        ColorPalettePastel1,
        ColorPalettePastel2,
        ColorPalettePaired,
        ColorPaletteAccent,
        ColorPaletteDark2,
        ColorPaletteSet1,
        ColorPaletteSet2,
        ColorPaletteSet3,
        ColorPaletteTab10,
        ColorPaletteTab20,
        ColorPaletteTab20b,
        ColorPaletteTab20c,
        ColorPaletteCustom
    ]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Color Palette"


class ColorAxisClass(Config):
    name: Literal["Class"] = "Class"
    value: Literal["Class"] = "Class"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Class"


class ColorAxisIndex(Config):
    name: Literal["Index"] = "Index"
    value: Literal["Index"] = "Index"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Index"


class ColorAxisTrack(Config):
    name: Literal["Track"] = "Track"
    value: Literal["Track"] = "Track"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Track"


class ConfigColorAxis(Config):
    """
        Determines bounding box colors based on class, index or track ID.
    """
    name: Literal["ConfigColorAxis"] = "ConfigColorAxis"
    value: Union[ColorAxisClass, ColorAxisIndex, ColorAxisTrack]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Color Axis"


class ConfigRadius(Config):
    """
        Radius of the circle in pixels.
    """
    name: Literal["ConfigRadius"] = "ConfigRadius"
    value: int = Field(default=0, ge=0, le=50)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Radius"


class ConfigThickness(Config):
    """
        Thickness of the bounding box in pixels.
    """
    name: Literal["ConfigThickness"] = "ConfigThickness"
    value: int = Field(ge=1, le=10)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Thickness"


class DrawBboxConfigs(Configs):
    configColorAxis: ConfigColorAxis
    configColorPalette: ConfigColorPalette
    configThickness: ConfigThickness
    configRadius: ConfigRadius


    class Config:
        title = "Draw Bounding Box Configurations"


class InputDetections(Input):
    name: Literal["inputDetections"] = "inputDetections"
    value: List[Detection]
    type: str = "list"

    class Config:
        title = "Detections"


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"
    class Config:
        title = "Image"


class DrawBboxInputs(Inputs):
    inputImage: InputImage
    inputDetections: InputDetections

    class Config:
        title = "Draw Bounding Box Inputs"


class DrawBboxRequest(Request):
    inputs: Union[DrawBboxInputs]
    configs: DrawBboxConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class DrawBboxOutputs(Outputs):
    outputImage: OutputImage

    class Config:
        title = "Draw Bounding Box Outputs"


class DrawBboxResponse(Response):
    outputs: DrawBboxOutputs

    class Config:
        title = "Draw Bounding Box Response"


class DrawBboxExecutor(Config):
    name: Literal["DrawBoundingBox"] = "DrawBoundingBox"
    value: Union[DrawBboxRequest, DrawBboxResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Draw Bounding Box Executor"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[DrawBboxExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor

    class Config:
        title = "Package Configurations"


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["DrawBoundingBox"] = "DrawBoundingBox"

    class Config:
        title = "Package Model"
