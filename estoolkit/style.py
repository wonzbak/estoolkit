# coding: utf-8

"""Style for prompt_toolkit
"""

from prompt_toolkit.token import Token
from prompt_toolkit.styles import style_from_dict


# all styles
style = style_from_dict({
    Token: '#ffffff',

    # Token.Command: '#ff0000',
    Token.Toolbar: '#333333 bg:#ffffff',

    # Url
    Token.Protocol: '#ff0000',
    Token.Host: '#0000cc',
    Token.PortSep: '#00FFFF',
    Token.Port: '#0000ff',

    # Prompt.
    # Token.Username: '#884444',
    # Token.At:       '#00aa00',
    # Token.Colon:    '#00aa00',
    # Token.Pound:    '#00aa00',
    # Token.Host:     '#000088 bg:#aaaaff',
    # Token.Path:     '#884444 underline',

})
