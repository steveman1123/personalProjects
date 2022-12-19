Public Class Form1


    Private Sub txtTest_TextChanged(ByVal sender As System.Object, ByVal i As System.EventArgs) Handles txtTest.TextChanged
        Dim chrTest As Char = Me.txtTest.Text.ToLower
        Dim A As Single = 0
        Dim B As Single = 0
        Dim C As Single = 0
        Dim D As Single = 0
        Dim E As Single = 0
        Dim F As Single = 0
        Dim G As Single = 0
        Dim H As Single = 0

        Select Case chrTest
            Case "0"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "1"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "2"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "3"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "4"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "5"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "6"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "7"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "8"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "9"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "a"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "b"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "c"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "d"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "e"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "f"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "g"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "h"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "i"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "j"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "l"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "n"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "o"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "p"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "q"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "r"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "s"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "t"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "u"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "v"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case "y"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Red
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Red
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "z"
                pnlA.BackColor = Color.Red
                pnlB.BackColor = Color.Red
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Red
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "."
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Red
            Case "-"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Red
                pnlH.BackColor = Color.Black
            Case "_"
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Red
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
            Case Else
                pnlA.BackColor = Color.Black
                pnlB.BackColor = Color.Black
                pnlC.BackColor = Color.Black
                pnlD.BackColor = Color.Black
                pnlE.BackColor = Color.Black
                pnlF.BackColor = Color.Black
                pnlG.BackColor = Color.Black
                pnlH.BackColor = Color.Black
        End Select
        Me.lblA1.Text = Math.Abs(Val(Me.pnlA.BackColor = Color.Black))
        Me.lblB1.Text = Math.Abs(Val(Me.pnlB.BackColor = Color.Black))
        Me.lblC1.Text = Math.Abs(Val(Me.pnlC.BackColor = Color.Black))
        Me.lblD1.Text = Math.Abs(Val(Me.pnlD.BackColor = Color.Black))
        Me.lblE1.Text = Math.Abs(Val(Me.pnlE.BackColor = Color.Black))
        Me.lblF1.Text = Math.Abs(Val(Me.pnlF.BackColor = Color.Black))
        Me.lblG1.Text = Math.Abs(Val(Me.pnlG.BackColor = Color.Black))
        Me.lblH1.Text = Math.Abs(Val(Me.pnlH.BackColor = Color.Black))

    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        pnlA.BackColor = Color.Black
        pnlB.BackColor = Color.Black
        pnlC.BackColor = Color.Black
        pnlD.BackColor = Color.Black
        pnlE.BackColor = Color.Black
        pnlF.BackColor = Color.Black
        pnlG.BackColor = Color.Black
        pnlH.BackColor = Color.Black
    End Sub
End Class
