Public Class Form1
    'Steven Williams
    '10/11/12

    Dim dblTotal As Double
    Dim intBand1 As Integer
    Dim intBand2 As Integer
    Dim dblBand3 As Double
    Dim intBand4 As Integer
#Region " 1st Band "
    Private Sub cmb1_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmb1.SelectedIndexChanged
        Me.lblAns.Text = ""
        Select Case cmb1.Text
            Case Is = "Black"
                intBand1 = 0
                Panel1.BackColor = Color.Black
            Case Is = "Brown"
                intBand1 = 1
                Panel1.BackColor = Color.Brown
            Case Is = "Red"
                intBand1 = 2
                Panel1.BackColor = Color.Red
            Case Is = "Orange"
                intBand1 = 3
                Panel1.BackColor = Color.Orange
            Case Is = "Yellow"
                intBand1 = 4
                Panel1.BackColor = Color.Yellow
            Case Is = "Green"
                intBand1 = 5
                Panel1.BackColor = Color.Green
            Case Is = "Blue"
                intBand1 = 6
                Panel1.BackColor = Color.Blue
            Case Is = "Violet"
                intBand1 = 7
                Panel1.BackColor = Color.Violet
            Case Is = "Grey"
                intBand1 = 8
                Panel1.BackColor = Color.Gray
            Case Is = "White"
                intBand1 = 9
                Panel1.BackColor = Color.White
            Case Else
                intBand1 = Nothing
                Panel1.BackColor = Color.SandyBrown
        End Select
    End Sub
#End Region
#Region " 2nd Band "

    Private Sub cmb2_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmb2.SelectedIndexChanged
        Me.lblAns.Text = ""
        Select Case cmb2.Text
            Case Is = "Black"
                intBand2 = 0
                Panel2.BackColor = Color.Black
            Case Is = "Brown"
                intBand2 = 1
                Panel2.BackColor = Color.Brown
            Case Is = "Red"
                intBand2 = 2
                Panel2.BackColor = Color.Red
            Case Is = "Orange"
                intBand2 = 3
                Panel2.BackColor = Color.Orange
            Case Is = "Yellow"
                intBand2 = 4
                Panel2.BackColor = Color.Yellow
            Case Is = "Green"
                intBand2 = 5
                Panel2.BackColor = Color.Green
            Case Is = "Blue"
                intBand2 = 6
                Panel2.BackColor = Color.Blue
            Case Is = "Violet"
                intBand2 = 7
                Panel2.BackColor = Color.Violet
            Case Is = "Grey"
                intBand2 = 8
                Panel2.BackColor = Color.Gray
            Case Is = "White"
                intBand2 = 9
                Panel2.BackColor = Color.White
            Case Else
                intBand2 = Nothing
                Panel2.BackColor = Color.SandyBrown
        End Select
    End Sub
#End Region
#Region " 3rd Band "
    Private Sub cmb3_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmb3.SelectedIndexChanged
        Me.lblAns.Text = ""
        Select Case cmb3.Text
            Case Is = "Silver"
                dblBand3 = 0.01
                Panel3.BackColor = Color.Silver
            Case Is = "Gold"
                dblBand3 = 0.1
                Panel3.BackColor = Color.Gold
            Case Is = "Black"
                dblBand3 = 1
                Panel3.BackColor = Color.Black
            Case Is = "Brown"
                dblBand3 = 10
                Panel3.BackColor = Color.Brown
            Case Is = "Red"
                dblBand3 = 100
                Panel3.BackColor = Color.Red
            Case Is = "Orange"
                dblBand3 = 1000
                Panel3.BackColor = Color.Orange
            Case Is = "Yellow"
                dblBand3 = 10000
                Panel3.BackColor = Color.Yellow
            Case Is = "Green"
                dblBand3 = 100000
                Panel3.BackColor = Color.Green
            Case Is = "Blue"
                dblBand3 = 1000000
                Panel3.BackColor = Color.Blue
            Case Is = "Violet"
                dblBand3 = 10000000
                Panel3.BackColor = Color.Violet
            Case Is = "Grey"
                dblBand3 = 100000000
                Panel3.BackColor = Color.Gray
            Case Is = "White"
                dblBand3 = 1000000000
                Panel3.BackColor = Color.White
            Case Else
                dblBand3 = Nothing
                Panel3.BackColor = Color.SandyBrown
        End Select
    End Sub
#End Region
#Region " 4th Band "
    Private Sub cmb4_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmb4.SelectedIndexChanged
        Me.lblAns.Text = ""
        Select Case Me.cmb4.Text
            Case Is = "None"
                intBand4 = 20
                Panel4.BackColor = Color.SandyBrown
            Case Is = "Silver"
                intBand4 = 10
                Panel4.BackColor = Color.Silver
            Case Is = "Gold"
                intBand4 = 5
                Panel4.BackColor = Color.Gold
            Case Else
                intBand4 = Nothing
                Panel4.BackColor = Color.SandyBrown
        End Select
    End Sub
#End Region
#Region " Calculate "
    Private Sub btnCalc_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnCalc.Click
        dblTotal = (10 * intBand1 + intBand2) * dblBand3
        Me.lblAns.Text = dblTotal & " ± " & intBand4 & "% Ω"
    End Sub
#End Region

    Private Sub btnReset_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles btnReset.Click
        Me.lblAns.Text = ""
        Me.cmb1.Text = ""
        Me.cmb2.Text = ""
        Me.cmb3.Text = ""
        Me.cmb4.Text = ""
        Me.Panel1.BackColor = Color.SandyBrown
        Me.Panel2.BackColor = Color.SandyBrown
        Me.Panel3.BackColor = Color.SandyBrown
        Me.Panel4.BackColor = Color.SandyBrown
    End Sub
End Class
