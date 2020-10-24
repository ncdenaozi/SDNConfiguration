"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
	    s3 = self.addSwitch( 's3' )
	    s4 = self.addSwitch( 's4' )
	    s5 = self.addSwitch( 's5' )


        # Add links
        self.addLink( H1, s1 )
        self.addLink( s1, s2,2,1 )
        self.addLink( s1, s3,3,1 )
	    self.addLink( s2, s5,3,1 )
	    self.addLink( s2, s4,2,1 )
	    self.addLink( s5, s4,2,2 )
	    self.addLink( s5, s3,3,3 )
	    self.addLink( s3, s4,2,3 )
	    self.addLink( s4, H2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }