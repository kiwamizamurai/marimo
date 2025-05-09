# Copyright 2024 Marimo. All rights reserved.
from __future__ import annotations

from typing import Any, Optional

from marimo._output.builder import h
from marimo._output.formatting import as_dom_node
from marimo._output.hypertext import Html
from marimo._output.rich_help import mddoc


@mddoc
def style(
    item: object, style: Optional[dict[str, Any]] = None, **kwargs: Any
) -> Html:
    """Wrap an object in a styled container.

    Example:
        ```python
        mo.style(item, styles={"max-height": "300px", "overflow": "auto"})
        mo.style(item, max_height="300px", overflow="auto")
        ```

    Args:
        item (object): An object to render as HTML.
        style (Optional[dict[str, Any]]): A dictionary of CSS styles,
            keyed by property name (e.g., "max-height"). Defaults to None.
        **kwargs (Any): Additional CSS styles specified as keyword arguments.
            Underscores in keyword arguments are converted to hyphens
            (e.g., `max_height` becomes `max-height`).

    Returns:
        Html: An HTML object representing the item wrapped in a div
                with the specified styles.
    """
    # Initialize combined_style with style dict if provided,
    # otherwise empty dict
    combined_style = style or {}

    # Add kwargs to combined_style, converting snake_case to kebab-case
    for key, value in kwargs.items():
        kebab_key = key.replace("_", "-")
        combined_style[kebab_key] = value

    style_str = ";".join(
        [f"{key}:{value}" for key, value in combined_style.items()]
    )
    return Html(h.div(children=as_dom_node(item).text, style=style_str))
