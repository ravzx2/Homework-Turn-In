Sub AllWorksheets()

Dim xSh As Worksheet
Application.ScreenUpdating = False
    
    For Each xSh In Worksheets
        xSh.Select
        Call StockMarket
    Next
    Application.ScreenUpdating = True
    
End Sub

Sub StockMarket()
Dim TickerName As String

Dim TickerTotal As Double
TickerTotal = 0

Dim TickerRow As Integer
TickerRow = 2

Dim TickerCount As Double
TickerCount = 1

Dim LastRow As Double
LastRow = Cells(Rows.Count, 1).End(xlUp).Row

Dim MaxIncrease As Double
MaxIncrease = 0

Dim MaxDecrease As Double
MaxDecrease = 0

Dim GreatestTotalVolume As Double
GreatestTotalVolume = 0

Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Ticker Volume"
Cells(1, 11).Value = "Yearly Change"
Cells(1, 12).Value = "Percent Change"
Cells(1, 15).Value = "Ticker"
Cells(1, 16).Value = "Value"
Cells(2, 14).Value = "Greatest % increase"
Cells(3, 14).Value = "Greatest % Decrease"
Cells(4, 14).Value = "Greatest Total Volume"

For I = 2 To LastRow

    If Cells((I - TickerCount + 1), 3).Value = 0 Then
        Cells((I - TickerCount + 1), 3).Value = 1
        
        Else
        
    End If
        
    If Cells(I + 1, 1).Value = Cells(I, 1).Value Then
    
        TickerTotal = TickerTotal + Cells(I, 7).Value
        TickerCount = TickerCount + 1
    
        Else
        TickerName = Cells(I, 1).Value
        TickerTotal = TickerTotal + Cells(I, 7).Value
        
        Cells(TickerRow, 9).Value = TickerName
        Cells(TickerRow, 10).Value = TickerTotal
        
        Cells(TickerRow, 11).Value = Cells(I, 6).Value - Cells((I - TickerCount + 1), 3).Value
        Cells(TickerRow, 12).Value = (Cells(I, 6).Value - Cells((I - TickerCount + 1), 3).Value) / (Cells((I - TickerCount + 1), 3).Value)
        TickerCount = 1
        
        TickerRow = TickerRow + 1
        TickerTotal = 0
        
    End If
    
    If Cells(I, 12).Value > MaxIncrease Then
        MaxIncrease = Cells(I, 12).Value
        
        Else
        Cells(2, 16).Value = MaxIncrease
        Cells(2, 15).Value = Cells(I, 9).Value
        
    End If
    
    If Cells(I, 12).Value < MaxDecrease Then
        MaxDecrease = Cells(I, 12).Value
        
        Else
        Cells(3, 16).Value = MaxDecrease
        Cells(3, 15).Value = Cells(I, 9).Value
        
    End If
    
    If Cells(I, 10).Value > GreatestTotalVolume Then
        GreatestTotalVolume = Cells(I, 10).Value
        
        Else
        Cells(4, 16).Value = GreatestTotalVolume
        Cells(4, 15).Value = Cells(I, 9).Value
        
    End If

Next I

End Sub
