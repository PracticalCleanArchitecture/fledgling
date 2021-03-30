# -*- coding: utf8 -*-
import click

from fledgling.cli.command.create_task import create_task
from fledgling.cli.command.event_loop import event_loop


if __name__ == '__main__':
    cli = click.Group()

    create_task_command = click.Command(
        'create-task',
        callback=create_task,
        params=[
            click.Option(
                param_decls=['--brief'],
                required=True,
                type=str,
            )
        ]
    )
    cli.add_command(create_task_command)

    event_loop_command = click.Command('event-loop', callback=event_loop)
    cli.add_command(event_loop_command)
    cli()
