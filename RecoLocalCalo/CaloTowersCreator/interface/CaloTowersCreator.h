#ifndef RECOLOCALCALO_CALOTOWERSCREATOR_CALOTOWERSCREATOR_H
#define RECOLOCALCALO_CALOTOWERSCREATOR_CALOTOWERSCREATOR_H 1

#include "FWCore/Framework/interface/EDProducer.h"
#include "DataFormats/Common/interface/EDProduct.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Handle.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "Geometry/CaloTopology/interface/HcalTopology.h"

#include "RecoLocalCalo/CaloTowersCreator/interface/CaloTowersCreationAlgo.h"

/** \class CaloTowersCreator
  *  
  * $Date: 2006/02/27 23:09:56 $
  * $Revision: 1.3 $
  * \author J. Mans - Minnesota
  */
class CaloTowersCreator : public edm::EDProducer {
public:
  explicit CaloTowersCreator(const edm::ParameterSet& ps);
  virtual ~CaloTowersCreator() { }
  virtual void produce(edm::Event& e, const edm::EventSetup& c);
private:
  CaloTowersCreationAlgo algo_;
  std::string hbheLabel_,hoLabel_,hfLabel_;
  std::vector<std::string> ecalLabels_;
  bool allowMissingInputs_;
};

#endif
