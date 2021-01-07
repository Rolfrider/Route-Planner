import 'package:flutter/material.dart';
import 'package:route_planner/map_view.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Route Planner",
      theme: ThemeData(primarySwatch: Colors.blue),
      home: MapView(),
    );
  }
}
