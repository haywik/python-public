from rich.console import Console
from rich.table import Table

c = Console()

t = Table(show_header=True,header_style="bold magenta")
t.add_column("C1", style="dim",width=20)
t.add_column("C2", style="dim",width=20)
t.add_column("C3", style="dim",width=20)

web1 = "test\ntest2\ntest3\n"
#
web2="pest1\npest2\nptest3\n"

t.add_row(web1,web2)

c.print(t)
