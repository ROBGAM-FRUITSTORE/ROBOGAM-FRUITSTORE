
"use strict";

let FaceDetections = require('./FaceDetections.js');
let Gesture = require('./Gesture.js');
let HogDetections = require('./HogDetections.js');
let LegDetections = require('./LegDetections.js');
let HogDetection = require('./HogDetection.js');
let FaceDetection = require('./FaceDetection.js');
let HeadPanTilt = require('./HeadPanTilt.js');
let DetectedPerson = require('./DetectedPerson.js');
let FollowMeResponse = require('./FollowMeResponse.js');
let DetectedObject = require('./DetectedObject.js');
let Rectangle = require('./Rectangle.js');
let FaceRecognitionGoal = require('./FaceRecognitionGoal.js');
let FaceRecognitionActionResult = require('./FaceRecognitionActionResult.js');
let FaceRecognitionActionGoal = require('./FaceRecognitionActionGoal.js');
let FaceRecognitionFeedback = require('./FaceRecognitionFeedback.js');
let FaceRecognitionAction = require('./FaceRecognitionAction.js');
let FaceRecognitionActionFeedback = require('./FaceRecognitionActionFeedback.js');
let FaceRecognitionResult = require('./FaceRecognitionResult.js');

module.exports = {
  FaceDetections: FaceDetections,
  Gesture: Gesture,
  HogDetections: HogDetections,
  LegDetections: LegDetections,
  HogDetection: HogDetection,
  FaceDetection: FaceDetection,
  HeadPanTilt: HeadPanTilt,
  DetectedPerson: DetectedPerson,
  FollowMeResponse: FollowMeResponse,
  DetectedObject: DetectedObject,
  Rectangle: Rectangle,
  FaceRecognitionGoal: FaceRecognitionGoal,
  FaceRecognitionActionResult: FaceRecognitionActionResult,
  FaceRecognitionActionGoal: FaceRecognitionActionGoal,
  FaceRecognitionFeedback: FaceRecognitionFeedback,
  FaceRecognitionAction: FaceRecognitionAction,
  FaceRecognitionActionFeedback: FaceRecognitionActionFeedback,
  FaceRecognitionResult: FaceRecognitionResult,
};
