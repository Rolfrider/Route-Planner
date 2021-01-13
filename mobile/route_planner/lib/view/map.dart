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

  final _bounds = CameraTargetBounds(MapModel.bounds);

  @override
  void initState() {
    super.initState();
  }

  MapModel model;

  @override
  Widget build(BuildContext context) {
    model = context.watch<MapModel>();
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
            SafeArea(
              child: Align(
                alignment: Alignment.bottomRight,
                child: Padding(
                  padding: const EdgeInsets.only(right: 10.0, bottom: 10.0),
                  child: ClipOval(
                    child: Material(
                      // button color
                      child: InkWell(
                        splashColor: Colors.blue, // inkwell color
                        child: SizedBox(
                          width: 56,
                          height: 56,
                          child: Icon(Icons.navigation),
                        ),
                        onTap: () {
                          model.findRoute();
                        },
                      ),
                    ),
                  ),
                ),
              ),
            ),
            if (model.isLoading)
              Container(
                width: width,
                height: height,
                alignment: Alignment.center,
                color: Colors.white60,
                child: CircularProgressIndicator(
                  valueColor: AlwaysStoppedAnimation<Color>(Colors.blueGrey),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
