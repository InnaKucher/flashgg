import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD



from os import environ
usePrivateSQlite=True

if usePrivateSQlite:
    from CondCore.DBCommon.CondDBSetup_cfi import *
    import os


#============================================Apply MET correction and syst.=================================================#

def runMETs(process,isMC):
    #================================ Get the most recent JEC ==================================================================#
    # Setup the private SQLite -- Ripped from PhysicsTools/PatAlgos/test/corMETFromMiniAOD.py
    era = "Spring16_25nsV6"
    if isMC : 
        era += "_MC"
    else :
        era += "_DATA"
        
    dBFile = os.path.expandvars(era+".db")
    
    print dBFile
    if usePrivateSQlite:
        process.jec = cms.ESSource("PoolDBESSource",
                                   CondDBSetup,
                                   connect = cms.string("sqlite_file:"+dBFile),
                                   toGet =  cms.VPSet(
                cms.PSet(
                    record = cms.string("JetCorrectionsRecord"),
                    tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PF"),
                    label= cms.untracked.string("AK4PF")
                    ),
                cms.PSet(
                        record = cms.string("JetCorrectionsRecord"),
                        tag = cms.string("JetCorrectorParametersCollection_"+era+"_AK4PFchs"),
                        label= cms.untracked.string("AK4PFchs")
                        ),
                )
                                   )
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')
#===========================================================================================================================#
        
        
        
        runMetCorAndUncFromMiniAOD(process, metType="PF",
                                   jetCollUnskimmed="slimmedJets",
                                   electronColl="slimmedElectrons",
                                   photonColl="slimmedPhotons",
                                   muonColl="slimmedMuons",
                                   tauColl="slimmedTaus",
                                   #reclusterJets = False,
                                   recoMetFromPFCs=True,
                                   pfCandColl = "packedPFCandidates",
                                   postfix="",
                                   isData=(not isMC),
                                   )
        
#===========================================================================================================================#

def setMetCorr(process, metCorr):
    
    process.pfMEtMultShiftCorr.paramaters                 = metCorr
    process.patPFMetTxyCorr.paramaters                    = metCorr
    process.multPhiCorrParams_T0rtTxy_25ns                = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T0rtT1Txy_25ns              = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T0rtT1T2Txy_25ns            = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T0pcTxy_25ns                = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T0pcT1Txy_25ns              = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T0pcT1T2Txy_25ns            = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T1Txy_25ns                  = cms.VPSet( pset for pset in metCorr)
    process.multPhiCorrParams_T1T2Txy_25ns                = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T0pcT1SmearTxy_25ns      = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T0pcT1T2SmearTxy_25ns    = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T0pcT1T2Txy_25ns         = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T0pcT1Txy_25ns           = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T0pcTxy_25ns             = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T1SmearTxy_25ns          = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T1T2SmearTxy_25ns        = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T1T2Txy_25ns             = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_T1Txy_25ns               = cms.VPSet( pset for pset in metCorr)
    process.patMultPhiCorrParams_Txy_25ns                 = cms.VPSet( pset for pset in metCorr)
    