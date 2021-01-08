import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:route_planner/map_view.dart';
import 'package:route_planner/model/map.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Route Planner",
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ChangeNotifierProvider(
        create: (context) => MapModel(),
        child: MapView(),
      ),
    );
  }
}
