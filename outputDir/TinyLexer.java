// Generated from EBNF.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TinyLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.0", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		INTEGER=10, FLOAT=11, CHAR=12, BOOL=13, LETTER=14, DIGIT=15, WS=16, LPAREN=17, 
		RPAREN=18, LBRACE=19, RBRACE=20, SEMI=21, PLUS=22, MINUS=23, TIMES=24, 
		DIV=25, ErrorChar=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"INTEGER", "FLOAT", "CHAR", "BOOL", "LETTER", "DIGIT", "WS", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "SEMI", "PLUS", "MINUS", "TIMES", "DIV", 
			"ErrorChar"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "'='", "'if'", "'else'", "'while'", "'int'", "'float'", 
			"'char'", "'bool'", null, null, null, null, null, null, null, "'('", 
			"')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "INTEGER", 
			"FLOAT", "CHAR", "BOOL", "LETTER", "DIGIT", "WS", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "SEMI", "PLUS", "MINUS", "TIMES", "DIV", "ErrorChar"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public TinyLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "EBNF.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001a\u0099\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0004\t]"+
		"\b\t\u000b\t\f\t^\u0001\n\u0004\nb\b\n\u000b\n\f\nc\u0001\n\u0001\n\u0004"+
		"\nh\b\n\u000b\n\f\ni\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\fy\b\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000f"+
		"\u0080\b\u000f\u000b\u000f\f\u000f\u0081\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001"+
		"\u0019\u0001\u0019\u0000\u0000\u001a\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012"+
		"%\u0013\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a\u0001\u0000"+
		"\u0003\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t\n\r\r  \u009d\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00037\u0001\u0000\u0000\u0000"+
		"\u00059\u0001\u0000\u0000\u0000\u0007<\u0001\u0000\u0000\u0000\tA\u0001"+
		"\u0000\u0000\u0000\u000bG\u0001\u0000\u0000\u0000\rK\u0001\u0000\u0000"+
		"\u0000\u000fQ\u0001\u0000\u0000\u0000\u0011V\u0001\u0000\u0000\u0000\u0013"+
		"\\\u0001\u0000\u0000\u0000\u0015a\u0001\u0000\u0000\u0000\u0017k\u0001"+
		"\u0000\u0000\u0000\u0019x\u0001\u0000\u0000\u0000\u001bz\u0001\u0000\u0000"+
		"\u0000\u001d|\u0001\u0000\u0000\u0000\u001f\u007f\u0001\u0000\u0000\u0000"+
		"!\u0085\u0001\u0000\u0000\u0000#\u0087\u0001\u0000\u0000\u0000%\u0089"+
		"\u0001\u0000\u0000\u0000\'\u008b\u0001\u0000\u0000\u0000)\u008d\u0001"+
		"\u0000\u0000\u0000+\u008f\u0001\u0000\u0000\u0000-\u0091\u0001\u0000\u0000"+
		"\u0000/\u0093\u0001\u0000\u0000\u00001\u0095\u0001\u0000\u0000\u00003"+
		"\u0097\u0001\u0000\u0000\u000056\u0005,\u0000\u00006\u0002\u0001\u0000"+
		"\u0000\u000078\u0005=\u0000\u00008\u0004\u0001\u0000\u0000\u00009:\u0005"+
		"i\u0000\u0000:;\u0005f\u0000\u0000;\u0006\u0001\u0000\u0000\u0000<=\u0005"+
		"e\u0000\u0000=>\u0005l\u0000\u0000>?\u0005s\u0000\u0000?@\u0005e\u0000"+
		"\u0000@\b\u0001\u0000\u0000\u0000AB\u0005w\u0000\u0000BC\u0005h\u0000"+
		"\u0000CD\u0005i\u0000\u0000DE\u0005l\u0000\u0000EF\u0005e\u0000\u0000"+
		"F\n\u0001\u0000\u0000\u0000GH\u0005i\u0000\u0000HI\u0005n\u0000\u0000"+
		"IJ\u0005t\u0000\u0000J\f\u0001\u0000\u0000\u0000KL\u0005f\u0000\u0000"+
		"LM\u0005l\u0000\u0000MN\u0005o\u0000\u0000NO\u0005a\u0000\u0000OP\u0005"+
		"t\u0000\u0000P\u000e\u0001\u0000\u0000\u0000QR\u0005c\u0000\u0000RS\u0005"+
		"h\u0000\u0000ST\u0005a\u0000\u0000TU\u0005r\u0000\u0000U\u0010\u0001\u0000"+
		"\u0000\u0000VW\u0005b\u0000\u0000WX\u0005o\u0000\u0000XY\u0005o\u0000"+
		"\u0000YZ\u0005l\u0000\u0000Z\u0012\u0001\u0000\u0000\u0000[]\u0003\u001d"+
		"\u000e\u0000\\[\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\\\u0001"+
		"\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_\u0014\u0001\u0000\u0000"+
		"\u0000`b\u0003\u001d\u000e\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000"+
		"\u0000\u0000ca\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0001"+
		"\u0000\u0000\u0000eg\u0005.\u0000\u0000fh\u0003\u001d\u000e\u0000gf\u0001"+
		"\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000"+
		"ij\u0001\u0000\u0000\u0000j\u0016\u0001\u0000\u0000\u0000kl\u0005\'\u0000"+
		"\u0000lm\t\u0000\u0000\u0000mn\u0005\'\u0000\u0000n\u0018\u0001\u0000"+
		"\u0000\u0000op\u0005t\u0000\u0000pq\u0005r\u0000\u0000qr\u0005u\u0000"+
		"\u0000ry\u0005e\u0000\u0000st\u0005f\u0000\u0000tu\u0005a\u0000\u0000"+
		"uv\u0005l\u0000\u0000vw\u0005s\u0000\u0000wy\u0005e\u0000\u0000xo\u0001"+
		"\u0000\u0000\u0000xs\u0001\u0000\u0000\u0000y\u001a\u0001\u0000\u0000"+
		"\u0000z{\u0007\u0000\u0000\u0000{\u001c\u0001\u0000\u0000\u0000|}\u0007"+
		"\u0001\u0000\u0000}\u001e\u0001\u0000\u0000\u0000~\u0080\u0007\u0002\u0000"+
		"\u0000\u007f~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000"+
		"\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0084\u0006\u000f\u0000\u0000"+
		"\u0084 \u0001\u0000\u0000\u0000\u0085\u0086\u0005(\u0000\u0000\u0086\""+
		"\u0001\u0000\u0000\u0000\u0087\u0088\u0005)\u0000\u0000\u0088$\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0005{\u0000\u0000\u008a&\u0001\u0000\u0000\u0000"+
		"\u008b\u008c\u0005}\u0000\u0000\u008c(\u0001\u0000\u0000\u0000\u008d\u008e"+
		"\u0005;\u0000\u0000\u008e*\u0001\u0000\u0000\u0000\u008f\u0090\u0005+"+
		"\u0000\u0000\u0090,\u0001\u0000\u0000\u0000\u0091\u0092\u0005-\u0000\u0000"+
		"\u0092.\u0001\u0000\u0000\u0000\u0093\u0094\u0005*\u0000\u0000\u00940"+
		"\u0001\u0000\u0000\u0000\u0095\u0096\u0005/\u0000\u0000\u00962\u0001\u0000"+
		"\u0000\u0000\u0097\u0098\t\u0000\u0000\u0000\u00984\u0001\u0000\u0000"+
		"\u0000\u0006\u0000^cix\u0081\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}