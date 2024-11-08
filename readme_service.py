# readme_service.py
from graphviz import Digraph

def create_flowchart():
    dot = Digraph(comment='Education-based Application Flowchart')
    dot.node('A', 'Start')
    dot.node('B', 'User Authentication')
    dot.node('C', 'Access Education Content')
    dot.node('D', 'End')
    
    dot.edges(['AB', 'BC', 'CD'])
    dot.render('education_flowchart', format='png', cleanup=True)

def update_readme():
    create_flowchart()
    
    readme_content = """
    # My FastAPI Application

    This is a simple FastAPI application with a dummy API endpoint.

    ![Education Flowchart](education_flowchart.png)
    """
    
    with open("ReadMe.md", "w") as f:
        f.write(readme_content)