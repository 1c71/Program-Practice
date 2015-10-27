import QtQuick 1.0
 
Rectangle {
    width: 200
    height: 200
    color: "white"
 
    Text {
        text: "Hello World"
        anchors.centerIn: parent
        font.pixelSize: 24
        color: 'black'
       
        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.log("Mouse clicked!", parent.color)
                if (parent.color == "#000000")
                    parent.color = 'blue';
                else
                    parent.color = 'black';                
            }
        }
    }
}