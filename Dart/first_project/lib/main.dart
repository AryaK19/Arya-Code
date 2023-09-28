import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: Home()
));

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('my First App'),
        centerTitle: true,
        backgroundColor: Colors.green[300],
      ),
      body: Center(
        child: Image(
          image:AssetImage('Assets/pxfuel.jpg')
        ),
      ),
      floatingActionButton:FloatingActionButton(
        onPressed: () {  },

        child: Text('Click'),
        backgroundColor: Colors.green[300],
      ) ,
    );
  }
}
