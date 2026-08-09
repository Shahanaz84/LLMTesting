from langchain_core.messages import AIMessage
from tutor_chain import prompt,outputParser,chain

def test_unit_prompt_fills_variable():
    msg = prompt.format(topic="hemant")
    assert "hemant" in msg           #variable landed
    assert "beginner" in msg        #instruction intact
    print(msg)

def test_unit_parser_returns_plain_string():
    out = outputParser.invoke(AIMessage(content="hello world"))
    assert isinstance(out,str) #string, not an object
    assert out == "hello world"

def test_chain_end_to_end():
    out = chain.invoke({"topic":""})
    assert "variables" in out.lower()
    assert len(out)> 25
    assert "error" not in out.lower()