# -*- coding: utf-8 -*-
#source: http://www.alexkuhl.org/code/
'''
Copyright (c) 2010, Alex Kuhl, http://www.alexkuhl.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of the author nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import sys, urllib, numpy, datetime
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import xlrd

FIRSTYEAR = 1997 # the first year the oil history has consistent data
maxoilchange = 0
minoilchange = 0
avgoilchangeu = 0
avgoilchanged = 0
maxgaschange = 0
mingaschange = 0
avggaschangeu = 0 
avggaschanged = 0

# each of the xls files we use only has two columns of importance
# column 0 for date and one other for data, so specify the other
def parse_xls( filename, datacol ):
    global maxoilchange, minoilchange, avgoilchangeu, avgoilchanged, maxgaschange, mingaschange, avggaschangeu, avggaschanged
    book = xlrd.open_workbook( filename )
    sh = book.sheet_by_index( 1 ) # sheet 1 because 0 is the "title" page in ours
    temp = []
    total = 0.0
    n = 0
    lastmonth = 1
    lastyear = FIRSTYEAR
    lastval = 0
    current = 0
    isgas = ( "gas" == filename[ :3 ] )
    totalchangeu = 0 # change up
    totalchanged = 0 # change down

    start = 3 # skip first 3 rows, contain junk
    while True: 
        year = xlrd.xldate_as_tuple( sh.cell_value( start, 0 ), 0 )[ 0 ]
        if year >= FIRSTYEAR:
            lastval = sh.cell_value( start, datacol )
            break
        start += 1
    for x in xrange( start, sh.nrows ): 
        date = xlrd.xldate_as_tuple( sh.cell_value( x, 0 ), 0 )
        month = date[ 1 ]
        year = date[ 0 ]
        current = sh.cell_value( x, datacol )
        # check for max/min
        change = current - lastval
        if isgas:
            if change > maxgaschange:
                maxgaschange = change
            elif change < mingaschange:
                mingaschange = change
        else:
            if change > maxoilchange:
                maxoilchange = change
            elif change < minoilchange:
                minoilchange = change
        if change > 0:
            totalchangeu += change
        else:
            totalchanged += abs( change )
        # work on the monthly accumulation
        if month == lastmonth:
            total += current
            n += 1
        else:
            temp.append( [ datetime.date( *date[ :3 ] ) , total/n ] )
            total = sh.cell_value( x, datacol )
            n = 1
            lastmonth = month       
            lastyear = year
        lastval = current
    # take care of the last month missed in loop
    if month == lastmonth:
        temp.append( [ datetime.date( *date[ :3 ] ), total/n ] )
    # averages
    if isgas:
        avggaschangeu = totalchangeu/(sh.nrows-start)
        avggaschanged = totalchanged/(sh.nrows-start)
    else:
        avgoilchangeu = totalchangeu/(sh.nrows-start)
        avgoilchanged = totalchanged/(sh.nrows-start)
    return temp

def split_columns( data ):
    col1 = [ ]
    col2 = [ ]
    for row in data:
        col1.append( row[ 0 ] )
        col2.append( row[ 1 ] )
    return col1, col2

# get the xls data
gasurl = 'http://tonto.eia.doe.gov/oog/ftparea/wogirs/xls/pswrgvwnus.xls'
gasfile = open( 'gasdata.xls', 'w' )
gasfile.write( urllib.urlopen( gasurl ).read( ) )
gasfile.close( )
gasdata = parse_xls( 'gasdata.xls', 3 )

oilurl = 'http://tonto.eia.doe.gov/dnav/pet/hist_xls/WTOTUSAw.xls'
oilfile = open( 'oildata.xls', 'w' )
oilfile.write( urllib.urlopen( oilurl ).read( ) )
oilfile.close( )
oildata = parse_xls( 'oildata.xls', 1 )

# change the data to be the percentage change from first data point
first = gasdata[ 0 ][ 1 ]
for row in gasdata:
    row[ 1 ] = ( row[ 1 ]-first )/first*100
first = oildata[ 0 ][ 1 ]
for row in oildata:
    row[ 1 ] = ( row[ 1 ]-first )/first*100

# get data ready for matplotlib
gdates, gdata = split_columns( gasdata )
odates, odata = split_columns( oildata )

# assure same length
longer = 0
shorter = 0
if len( odates ) < len( gdates ):
    s = len( odates )
    gdates = gdates[ :s ]
    gdata = gdata[ :s ]
elif len( gdates ) > len( odates ):
    s = len( gdates )
    odates = odates[ :s ]
    odata = odata[ :s ]

# set up date formatter
#N = len( odata )
#def format_date( d, pos = None ):
#    index = numpy.clip( int( d+.5 ), 0, N-1 )
#    return odates[ index ].strftime( "%m-%Y" )

# set up indices
#indices = numpy.arange( N )

#fig = plt.figure( )
#ax = fig.add_subplot( 111 )
plt.plot( gdates, gdata, 'r-', label='gas' )
plt.plot( odates, odata, 'b-', label='oil' )
plt.xlabel( 'Date' )
plt.ylabel( '% Change' )
plt.title( '% Change over Time -- Oil vs. Gas Price' )
plt.legend( ('gas', 'oil' ), loc='upper left' )
#ax.xaxis.set_major_formatter( ticker.FuncFormatter( format_date ) )
#fig.autofmt_xdate( )
plt.savefig( "plot.png" )

out = open( "results.txt", "w" )
out.write( "Max oil change: " + str( maxoilchange ) + "\n" )
out.write( "Min oil change: " + str( minoilchange ) + "\n" )
out.write( "Avg oil change up: " + str( avgoilchangeu ) + "\n" )
out.write( "Avg oil change down: " + str( avgoilchanged ) + "\n" )
out.write( "Max gas change: " + str( maxgaschange ) + "\n" )
out.write( "Min gas change: " + str( mingaschange ) + "\n" )
out.write( "Avg gas change up: " + str( avggaschangeu ) + "\n" )
out.write( "Avg gas change down: " + str( avggaschanged ) + "\n" )
