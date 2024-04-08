class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""

        for key, value in self.props.items():
            props_html += f" {key}=\"{value}\""
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"

    def __eq__(self,other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        result = ""
        if self.tag is None: 
            raise ValueError("No tag provided")
        if self.children is None:
            raise ValueError("No children provided")
        

        for child in self.children:
            result += child.to_html()
        
        result = f"<{self.tag}{self.props_to_html()}>" + result + f"</{self.tag}>"
        return result

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    