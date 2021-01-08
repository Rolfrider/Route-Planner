import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:route_planner/locator.dart';
import 'package:route_planner/model/map.dart';

class MapView extends StatefulWidget {
  @override
  _MapViewState createState() => _MapViewState();
}

class _MapViewState extends State<MapView> {
  CameraPosition _initialLocation =
      CameraPosition(target: LatLng(52.237049, 21.017532), zoom: 10);

  final _bounds = CameraTargetBounds(LatLngBounds(
      northeast: LatLng(52.368153, 21.271151),
      southwest: LatLng(52.097851, 20.851688)));

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    var model = context.watch<MapModel>();
    var height = MediaQuery.of(context).size.height;
    var width = MediaQuery.of(context).size.width;

    return Container(
      height: height,
      width: width,
      child: Scaffold(
        body: Stack(
          children: <Widget>[
            GoogleMap(
              markers: model.markers,
              myLocationEnabled: true,
              myLocationButtonEnabled: false,
              mapType: MapType.normal,
              zoomGesturesEnabled: true,
              initialCameraPosition: _initialLocation,
              cameraTargetBounds: _bounds,
              zoomControlsEnabled: false,
              polylines: model.polyline,
              onMapCreated: (GoogleMapController controller) {
                model.getCurrentLocation();
              },
              onTap: model.addMarker,
            ),
          ],
        ),
      ),
    );
  }
}
