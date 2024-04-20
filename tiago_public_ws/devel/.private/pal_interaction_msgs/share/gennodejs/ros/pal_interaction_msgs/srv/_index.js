
"use strict";

let SoundLocalisationService = require('./SoundLocalisationService.js')
let GetSpeechDuration = require('./GetSpeechDuration.js')
let ASRService = require('./ASRService.js')
let recognizerService = require('./recognizerService.js')

module.exports = {
  SoundLocalisationService: SoundLocalisationService,
  GetSpeechDuration: GetSpeechDuration,
  ASRService: ASRService,
  recognizerService: recognizerService,
};
