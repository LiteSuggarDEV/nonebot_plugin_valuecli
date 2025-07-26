from nonebot.plugin import require, PluginMetadata

require("nonebot_plugin_value")
require("nonebot_plugin_alconna")

__plugin_meta__ = PluginMetadata(
    name="ValueCLI",
    description="Manager for nonebot_plugin_value",
    usage="/money",
    type="application",
    homepage="https://github.com/LiteSuggarDEV/nonebot_plugin_valuecli",
    supported_adapters=None,
)