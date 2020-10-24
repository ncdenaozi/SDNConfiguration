#!/usr/bin/python

"""
This setup the topology in lab3-part1
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.link import Link, Intf, TCLink
import os 
from time import sleep
import sys

N=4

class Topology(Topo):
    fatN=0
    
    def __init__(self):
        self.fatN= N
        #create 3 list
        TotalhostNum=self.fatN*self.fatN/2
        host=[0 for i in range(TotalhostNum)]
        EdgeSwitchNum=self.fatN
        EdgeSwitch=[0 for i in range(EdgeSwitchNum)]
        CoreSwitchNum=self.fatN/2
        CoreSwitch=[0 for i in range(CoreSwitchNum)]
        "Create Topology."
        # Initialize topology
        Topo.__init__(self)
        #### There is a rule of naming the hosts and switch, so please follow the rules like "h1", "h2" or "s1", "s2" for hosts and switches!!!!
      
        # Add hosts
        for i in range(TotalhostNum):
            host[i] = self.addHost('h'+str(i))        
        # Add edge switches
        for j in range(EdgeSwitchNum):
            EdgeSwitch[j]=self.addSwitch('s'+str(j))
        # Add core switches
        for k in range(CoreSwitchNum):
            CoreSwitch[k]=self.addSwitch('s'+str(EdgeSwitchNum+k))
        
        #link host to edgeswitch
        count=0
        for i in range(TotalhostNum):
            self.addLink(host[i],EdgeSwitch[count])
            if((i+1)%(self.fatN/2)==0):
                count=count+1

        #link edgeswitch to coreswitch
        for j in range(EdgeSwitchNum):
            for k in range(CoreSwitchNum):
                self.addLink(EdgeSwitch[j],CoreSwitch[k])


# This is for "mn --custom"
topos = { 'mytopo': ( lambda: Topology() ) }
