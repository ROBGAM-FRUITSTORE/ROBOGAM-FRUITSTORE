
"use strict";

let GoToGoal = require('./GoToGoal.js');
let ExecuteParkingActionFeedback = require('./ExecuteParkingActionFeedback.js');
let VisualTrainingActionGoal = require('./VisualTrainingActionGoal.js');
let ExecuteParkingActionResult = require('./ExecuteParkingActionResult.js');
let GoToPOIAction = require('./GoToPOIAction.js');
let JoyTurboAction = require('./JoyTurboAction.js');
let GoToResult = require('./GoToResult.js');
let FollowWaypointsResult = require('./FollowWaypointsResult.js');
let GoToActionResult = require('./GoToActionResult.js');
let ExecuteParkingActionGoal = require('./ExecuteParkingActionGoal.js');
let GoToPOIResult = require('./GoToPOIResult.js');
let FollowWaypointsFeedback = require('./FollowWaypointsFeedback.js');
let GoToPOIActionGoal = require('./GoToPOIActionGoal.js');
let JoyTurboResult = require('./JoyTurboResult.js');
let GoToAction = require('./GoToAction.js');
let ExecuteParkingGoal = require('./ExecuteParkingGoal.js');
let GoToPOIFeedback = require('./GoToPOIFeedback.js');
let VisualTrainingGoal = require('./VisualTrainingGoal.js');
let ExecuteParkingAction = require('./ExecuteParkingAction.js');
let JoyPriorityFeedback = require('./JoyPriorityFeedback.js');
let FollowWaypointsGoal = require('./FollowWaypointsGoal.js');
let VisualTrainingAction = require('./VisualTrainingAction.js');
let GoToPOIActionFeedback = require('./GoToPOIActionFeedback.js');
let ExecuteParkingResult = require('./ExecuteParkingResult.js');
let FollowWaypointsAction = require('./FollowWaypointsAction.js');
let GoToPOIActionResult = require('./GoToPOIActionResult.js');
let JoyPriorityActionResult = require('./JoyPriorityActionResult.js');
let VisualTrainingActionFeedback = require('./VisualTrainingActionFeedback.js');
let ExecuteParkingFeedback = require('./ExecuteParkingFeedback.js');
let JoyPriorityResult = require('./JoyPriorityResult.js');
let JoyPriorityActionGoal = require('./JoyPriorityActionGoal.js');
let GoToActionFeedback = require('./GoToActionFeedback.js');
let JoyPriorityGoal = require('./JoyPriorityGoal.js');
let JoyTurboFeedback = require('./JoyTurboFeedback.js');
let JoyTurboActionResult = require('./JoyTurboActionResult.js');
let JoyPriorityActionFeedback = require('./JoyPriorityActionFeedback.js');
let FollowWaypointsActionFeedback = require('./FollowWaypointsActionFeedback.js');
let VisualTrainingFeedback = require('./VisualTrainingFeedback.js');
let JoyTurboActionGoal = require('./JoyTurboActionGoal.js');
let JoyTurboActionFeedback = require('./JoyTurboActionFeedback.js');
let GoToFeedback = require('./GoToFeedback.js');
let GoToPOIGoal = require('./GoToPOIGoal.js');
let FollowWaypointsActionGoal = require('./FollowWaypointsActionGoal.js');
let JoyPriorityAction = require('./JoyPriorityAction.js');
let GoToActionGoal = require('./GoToActionGoal.js');
let VisualTrainingResult = require('./VisualTrainingResult.js');
let VisualTrainingActionResult = require('./VisualTrainingActionResult.js');
let JoyTurboGoal = require('./JoyTurboGoal.js');
let FollowWaypointsActionResult = require('./FollowWaypointsActionResult.js');
let NavigationStatus = require('./NavigationStatus.js');
let Highways = require('./Highways.js');
let NiceMapTransformation = require('./NiceMapTransformation.js');
let VisualLocDB = require('./VisualLocDB.js');
let POI = require('./POI.js');
let PolarReadingScan = require('./PolarReadingScan.js');
let AvailableMaps = require('./AvailableMaps.js');
let ServiceStatus = require('./ServiceStatus.js');
let LaserImage = require('./LaserImage.js');
let MapConfiguration = require('./MapConfiguration.js');
let POIGroup = require('./POIGroup.js');
let MissedWaypoint = require('./MissedWaypoint.js');
let EulerAnglesStamped = require('./EulerAnglesStamped.js');
let EulerAngles = require('./EulerAngles.js');
let PolarReading = require('./PolarReading.js');
let TabletPOI = require('./TabletPOI.js');
let Waypoint = require('./Waypoint.js');
let Emergency = require('./Emergency.js');

module.exports = {
  GoToGoal: GoToGoal,
  ExecuteParkingActionFeedback: ExecuteParkingActionFeedback,
  VisualTrainingActionGoal: VisualTrainingActionGoal,
  ExecuteParkingActionResult: ExecuteParkingActionResult,
  GoToPOIAction: GoToPOIAction,
  JoyTurboAction: JoyTurboAction,
  GoToResult: GoToResult,
  FollowWaypointsResult: FollowWaypointsResult,
  GoToActionResult: GoToActionResult,
  ExecuteParkingActionGoal: ExecuteParkingActionGoal,
  GoToPOIResult: GoToPOIResult,
  FollowWaypointsFeedback: FollowWaypointsFeedback,
  GoToPOIActionGoal: GoToPOIActionGoal,
  JoyTurboResult: JoyTurboResult,
  GoToAction: GoToAction,
  ExecuteParkingGoal: ExecuteParkingGoal,
  GoToPOIFeedback: GoToPOIFeedback,
  VisualTrainingGoal: VisualTrainingGoal,
  ExecuteParkingAction: ExecuteParkingAction,
  JoyPriorityFeedback: JoyPriorityFeedback,
  FollowWaypointsGoal: FollowWaypointsGoal,
  VisualTrainingAction: VisualTrainingAction,
  GoToPOIActionFeedback: GoToPOIActionFeedback,
  ExecuteParkingResult: ExecuteParkingResult,
  FollowWaypointsAction: FollowWaypointsAction,
  GoToPOIActionResult: GoToPOIActionResult,
  JoyPriorityActionResult: JoyPriorityActionResult,
  VisualTrainingActionFeedback: VisualTrainingActionFeedback,
  ExecuteParkingFeedback: ExecuteParkingFeedback,
  JoyPriorityResult: JoyPriorityResult,
  JoyPriorityActionGoal: JoyPriorityActionGoal,
  GoToActionFeedback: GoToActionFeedback,
  JoyPriorityGoal: JoyPriorityGoal,
  JoyTurboFeedback: JoyTurboFeedback,
  JoyTurboActionResult: JoyTurboActionResult,
  JoyPriorityActionFeedback: JoyPriorityActionFeedback,
  FollowWaypointsActionFeedback: FollowWaypointsActionFeedback,
  VisualTrainingFeedback: VisualTrainingFeedback,
  JoyTurboActionGoal: JoyTurboActionGoal,
  JoyTurboActionFeedback: JoyTurboActionFeedback,
  GoToFeedback: GoToFeedback,
  GoToPOIGoal: GoToPOIGoal,
  FollowWaypointsActionGoal: FollowWaypointsActionGoal,
  JoyPriorityAction: JoyPriorityAction,
  GoToActionGoal: GoToActionGoal,
  VisualTrainingResult: VisualTrainingResult,
  VisualTrainingActionResult: VisualTrainingActionResult,
  JoyTurboGoal: JoyTurboGoal,
  FollowWaypointsActionResult: FollowWaypointsActionResult,
  NavigationStatus: NavigationStatus,
  Highways: Highways,
  NiceMapTransformation: NiceMapTransformation,
  VisualLocDB: VisualLocDB,
  POI: POI,
  PolarReadingScan: PolarReadingScan,
  AvailableMaps: AvailableMaps,
  ServiceStatus: ServiceStatus,
  LaserImage: LaserImage,
  MapConfiguration: MapConfiguration,
  POIGroup: POIGroup,
  MissedWaypoint: MissedWaypoint,
  EulerAnglesStamped: EulerAnglesStamped,
  EulerAngles: EulerAngles,
  PolarReading: PolarReading,
  TabletPOI: TabletPOI,
  Waypoint: Waypoint,
  Emergency: Emergency,
};
