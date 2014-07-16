import FWCore.ParameterSet.Config as cms

from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry

ebCutOff = 1.479

cutBasedElectronID_CSA14_50ns_V0_standalone_tight = cms.PSet(
    idName = cms.string("cutBasedElectronID-CSA14-50ns-V0-standalone-tight"),
    cutFlow = cms.VPSet(
        cms.PSet( cutName = cms.string("MinPtCut"),
                  minPt = cms.double(5.0),
                  needsAdditionalProducts = cms.bool(False),
                  isIgnored = cms.bool(False)                ),
        cms.PSet( cutName = cms.string("GsfEleSCEtaMultiRangeCut"),
                  useAbsEta = cms.bool(True),
                  allowedEtaRanges = cms.VPSet( 
                                  cms.PSet( minEta = cms.double(0.0), 
                                            maxEta = cms.double(ebCutOff) ),
                                  cms.PSet( minEta = cms.double(ebCutOff), 
                                            maxEta = cms.double(2.5) )
                                  ) ),
        cms.PSet( cutName = cms.string('GsfEleDEtaInCut'),
                  dEtaInCutValueEB = cms.double(0.007),
                  dEtaInCutValueEE = cms.double(0.007),
                  barrelCutOff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleDPhiInCut'),
                  dPhiInCutValueEB = cms.double(0.03),
                  dPhiInCutValueEE = cms.double(0.02),
                  barrelCutOff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleSigmaIEtaIEtaCut'),
                  sigmaIEtaIEtaCutValueEB = cms.double(0.01),
                  sigmaIEtaIEtaCutValueEE = cms.double(0.03),
                  barrelCutOff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleHadronicOverEMCut'),
                  hadronicOverEMCutValueEB = cms.double(0.12),
                  hadronicOverEMCutValueEE = cms.double(0.10),
                  barrelCutOff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleDxyCut'),
                  dxyCutValueEB = cms.double(0.02),
                  dxyCutValueEE = cms.double(0.02),
                  vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                  barrelCutoff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleDzCut'),
                  dzCutValueEB = cms.double(0.1),
                  dzCutValueEE = cms.double(0.1),
                  vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                  barrelCutoff = cms.double(ebCutOff) ),
        cms.PSet( cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                  eInverseMinusPInverseCutValueEB = cms.double(0.05),
                  eInverseMinusPInverseCutValueEE = cms.double(0.05),
                  barrelCutoff = cms.double(ebCutOff)),
        cms.PSet( cutName = cms.string('GsfEleDeltaBetaIsoCutStandalone'),
                  isoCutEBLowPt = cms.double(0.13),
                  isoCutEBHighPt = cms.double(0.13),
                  isoCutEELowPt = cms.double(0.13),
                  isoCutEEHighPt = cms.double(0.13),
                  isRelativeIso = cms.bool(True),
                  deltaBetaConstant = cms.double(0.5),
                  ptCutOff = cms.double(20.0),
                  barrelCutoff = cms.double(ebCutOff)),
        cms.PSet( cutName = cms.string('GsfEleConversionVetoCut'),
                  conversionSrc = cms.InputTag('conversions'),
                  beamspotSrc = cms.InputTag('offlineBeamSpot') ),
        cms.PSet( cutName = cms.string('GsfEleMissingHitsCut'),
                  maxMissingHitsEB = cms.uint32(0),
                  maxMissingHitsEE = cms.uint32(0),
                  barrelCutoff = cms.double(ebCutOff) )                   
    )
)

central_id_registry.register(cutBasedElectronID_CSA14_50ns_V0_standalone_tight.idName,
                             'f03cb12936e5aeed5b9975a9eb27a9c1')
