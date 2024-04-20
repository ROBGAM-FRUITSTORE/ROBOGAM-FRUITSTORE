
"use strict";

let ChangeSyncMap = require('./ChangeSyncMap.js')
let SaveMap = require('./SaveMap.js')
let GetSubMap = require('./GetSubMap.js')
let RenameMap = require('./RenameMap.js')
let ChangeBuilding = require('./ChangeBuilding.js')
let GetMapConfiguration = require('./GetMapConfiguration.js')
let DisableEmergency = require('./DisableEmergency.js')
let GetNodes = require('./GetNodes.js')
let SetPOI = require('./SetPOI.js')
let ChangeMap = require('./ChangeMap.js')
let GetPOI = require('./GetPOI.js')
let VisualLocRecognize = require('./VisualLocRecognize.js')
let SetMapConfiguration = require('./SetMapConfiguration.js')
let FinalApproachPose = require('./FinalApproachPose.js')
let SetSubMapFloor = require('./SetSubMapFloor.js')
let SafetyZone = require('./SafetyZone.js')
let RegisterSync = require('./RegisterSync.js')
let Acknowledgment = require('./Acknowledgment.js')
let ListMaps = require('./ListMaps.js')

module.exports = {
  ChangeSyncMap: ChangeSyncMap,
  SaveMap: SaveMap,
  GetSubMap: GetSubMap,
  RenameMap: RenameMap,
  ChangeBuilding: ChangeBuilding,
  GetMapConfiguration: GetMapConfiguration,
  DisableEmergency: DisableEmergency,
  GetNodes: GetNodes,
  SetPOI: SetPOI,
  ChangeMap: ChangeMap,
  GetPOI: GetPOI,
  VisualLocRecognize: VisualLocRecognize,
  SetMapConfiguration: SetMapConfiguration,
  FinalApproachPose: FinalApproachPose,
  SetSubMapFloor: SetSubMapFloor,
  SafetyZone: SafetyZone,
  RegisterSync: RegisterSync,
  Acknowledgment: Acknowledgment,
  ListMaps: ListMaps,
};
