from coalib.bearlib.languages.Language import Language


@Language
class g4:
	aliases = 'antlr4', 'grun'
	extensions = '.g4',
	comment_delimiters = '//',
	multiline_comment_delimiters = {'/*': '*/'}
	string_delimiters = {"'": "'"}
	multiline_string_delimiters = {}
	indent_types = {'{': '}'}
    encapsulators = {'(': ')', '[': ']'}
	keywords = [
	    'import', 'fragment', 'lexer',
	    'parser', 'grammar', 'returns',
	    'locals', 'throws', 'catch',
	    'finally', 'mode', 'options',
	    'tokens']
    special_chars = list(r'/**+-*/.;\,()[]{}\=<>|&^~?%!')
    string_delimiter_escape = {"'": "\\'"}