
"use strict";

let StartEnrollment = require('./StartEnrollment.js')
let SelectTexturedObject = require('./SelectTexturedObject.js')
let ChangeObjectRecognizerModel = require('./ChangeObjectRecognizerModel.js')
let AddTexturedObject = require('./AddTexturedObject.js')
let Recognizer = require('./Recognizer.js')
let SetDatabase = require('./SetDatabase.js')
let StopEnrollment = require('./StopEnrollment.js')

module.exports = {
  StartEnrollment: StartEnrollment,
  SelectTexturedObject: SelectTexturedObject,
  ChangeObjectRecognizerModel: ChangeObjectRecognizerModel,
  AddTexturedObject: AddTexturedObject,
  Recognizer: Recognizer,
  SetDatabase: SetDatabase,
  StopEnrollment: StopEnrollment,
};
