from graphviz import Digraph
import os

def create_flowchart_graphviz():
    dot = Digraph(comment='Education Application Flowchart')
    dot.node('A', 'Start')
    dot.node('B', 'Login Page')
    dot.node('C', 'Dashboard')
    dot.node('D', 'Courses')
    dot.node('E', 'End')
    dot.edges(['AB', 'BC', 'CD', 'DE'])
    dot.render('flowchart_graphviz.png', format='png', cleanup=True)

def create_flowchart_mermaid():
    mermaid_content = """
    graph TD
        A[Start] --> B[Login Page]
        B --> C[Dashboard]
        C --> D[Courses]
        D --> E[End]
    """
    with open("flowchart_mermaid.md", "w") as f:
        f.write(mermaid_content)

def update_readme():
    create_flowchart_graphviz()
    create_flowchart_mermaid()
    with open("ReadMe.md", "w") as f:
        f.write("# My FastAPI Application\n\n")
        f.write("This is a simple FastAPI application with a dummy API endpoint.\n\n")
        f.write("![Education Application Flowchart (Graphviz)](flowchart_graphviz.png)\n")
        f.write("```mermaid\n")
        with open("flowchart_mermaid.md", "r") as mdf:
            f.write(mdf.read())
        f.write("```\n")