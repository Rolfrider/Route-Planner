import 'package:http/http.dart' as http;
import 'dart:convert';

import 'model/point.dart';

const _url = "http://10.0.2.2:8000/planner/";

Future<List<Point>> routeFor(List<Point> points) async {
  final request = http.Request('GET', Uri.parse(_url));
  request.body = jsonEncode(points);
  return request
      .send()
      .then((response) => http.Response.fromStream(response))
      .then((response) {
    if (response.statusCode == 200) {
      Iterable l = jsonDecode(response.body);
      return List<Point>.from(l.map((e) => Point.fromJson(e)));
    } else {
      throw Exception("Failed to load route");
    }
  });
}
