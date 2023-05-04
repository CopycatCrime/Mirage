<<<<<<< HEAD
import traceback
import discord
from discord.ext import commands
import config


class Mirage(commands.Bot):
    def __init__(self, **kwargs):
        self.version = 1.0
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or('#'), intents=intents, **kwargs, pm_help=None,
                         help_attrs=dict(hidden=True))

    async def setup_hook(self) -> None:
        for extension in config.cogs:
            try:
                await self.load_extension(extension)
            except Exception as e:
                print('コグ : {0} を以下の理由で読み込むことができませんでした. {1.__class__.__name__}: {1}'.format(
                    extension, e))
        await self.tree.sync()

    async def on_ready(self):
        print('{0}　としてログインしました  (ID: {0.id})'.format(self.user))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            return

        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        error_msg = "```py\n" + error_msg + "\n```"
        await ctx.send(error_msg)


bot = Mirage()

bot.run(config.token)

=======
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sample_function():
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
>>>>>>> 3b5df9c (first commit)
