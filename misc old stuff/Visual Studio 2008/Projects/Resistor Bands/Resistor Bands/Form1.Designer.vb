<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.cmb1 = New System.Windows.Forms.ComboBox
        Me.cmb2 = New System.Windows.Forms.ComboBox
        Me.cmb3 = New System.Windows.Forms.ComboBox
        Me.cmb4 = New System.Windows.Forms.ComboBox
        Me.Panel1 = New System.Windows.Forms.Panel
        Me.pnlBack = New System.Windows.Forms.Panel
        Me.Panel4 = New System.Windows.Forms.Panel
        Me.Panel2 = New System.Windows.Forms.Panel
        Me.Panel3 = New System.Windows.Forms.Panel
        Me.lblAns = New System.Windows.Forms.Label
        Me.btnCalc = New System.Windows.Forms.Button
        Me.lbl1 = New System.Windows.Forms.Label
        Me.Label2 = New System.Windows.Forms.Label
        Me.Label3 = New System.Windows.Forms.Label
        Me.Label4 = New System.Windows.Forms.Label
        Me.btnReset = New System.Windows.Forms.Button
        Me.pnlBack.SuspendLayout()
        Me.SuspendLayout()
        '
        'cmb1
        '
        Me.cmb1.FormattingEnabled = True
        Me.cmb1.Items.AddRange(New Object() {"Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"})
        Me.cmb1.Location = New System.Drawing.Point(56, 8)
        Me.cmb1.Name = "cmb1"
        Me.cmb1.Size = New System.Drawing.Size(112, 21)
        Me.cmb1.TabIndex = 1
        '
        'cmb2
        '
        Me.cmb2.FormattingEnabled = True
        Me.cmb2.Items.AddRange(New Object() {"Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"})
        Me.cmb2.Location = New System.Drawing.Point(56, 40)
        Me.cmb2.Name = "cmb2"
        Me.cmb2.Size = New System.Drawing.Size(112, 21)
        Me.cmb2.TabIndex = 2
        '
        'cmb3
        '
        Me.cmb3.FormattingEnabled = True
        Me.cmb3.Items.AddRange(New Object() {"Silver", "Gold", "Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Grey", "White"})
        Me.cmb3.Location = New System.Drawing.Point(56, 72)
        Me.cmb3.Name = "cmb3"
        Me.cmb3.Size = New System.Drawing.Size(112, 21)
        Me.cmb3.TabIndex = 3
        '
        'cmb4
        '
        Me.cmb4.FormattingEnabled = True
        Me.cmb4.Items.AddRange(New Object() {"None", "Silver", "Gold"})
        Me.cmb4.Location = New System.Drawing.Point(56, 104)
        Me.cmb4.Name = "cmb4"
        Me.cmb4.Size = New System.Drawing.Size(112, 21)
        Me.cmb4.TabIndex = 4
        '
        'Panel1
        '
        Me.Panel1.BackColor = System.Drawing.Color.SandyBrown
        Me.Panel1.Location = New System.Drawing.Point(16, 136)
        Me.Panel1.Name = "Panel1"
        Me.Panel1.Size = New System.Drawing.Size(16, 36)
        Me.Panel1.TabIndex = 5
        '
        'pnlBack
        '
        Me.pnlBack.BackColor = System.Drawing.Color.SandyBrown
        Me.pnlBack.Controls.Add(Me.Panel4)
        Me.pnlBack.Location = New System.Drawing.Point(0, 136)
        Me.pnlBack.Name = "pnlBack"
        Me.pnlBack.Size = New System.Drawing.Size(168, 36)
        Me.pnlBack.TabIndex = 6
        '
        'Panel4
        '
        Me.Panel4.BackColor = System.Drawing.Color.SandyBrown
        Me.Panel4.Location = New System.Drawing.Point(128, 0)
        Me.Panel4.Name = "Panel4"
        Me.Panel4.Size = New System.Drawing.Size(16, 36)
        Me.Panel4.TabIndex = 8
        '
        'Panel2
        '
        Me.Panel2.BackColor = System.Drawing.Color.SandyBrown
        Me.Panel2.Location = New System.Drawing.Point(48, 136)
        Me.Panel2.Name = "Panel2"
        Me.Panel2.Size = New System.Drawing.Size(16, 36)
        Me.Panel2.TabIndex = 7
        '
        'Panel3
        '
        Me.Panel3.BackColor = System.Drawing.Color.SandyBrown
        Me.Panel3.Location = New System.Drawing.Point(80, 136)
        Me.Panel3.Name = "Panel3"
        Me.Panel3.Size = New System.Drawing.Size(16, 36)
        Me.Panel3.TabIndex = 8
        '
        'lblAns
        '
        Me.lblAns.Location = New System.Drawing.Point(0, 216)
        Me.lblAns.Name = "lblAns"
        Me.lblAns.Size = New System.Drawing.Size(120, 40)
        Me.lblAns.TabIndex = 7
        Me.lblAns.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        '
        'btnCalc
        '
        Me.btnCalc.BackColor = System.Drawing.Color.Green
        Me.btnCalc.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnCalc.ForeColor = System.Drawing.SystemColors.ControlText
        Me.btnCalc.Location = New System.Drawing.Point(0, 176)
        Me.btnCalc.Name = "btnCalc"
        Me.btnCalc.Size = New System.Drawing.Size(176, 40)
        Me.btnCalc.TabIndex = 8
        Me.btnCalc.Text = "Calculate Resistance"
        Me.btnCalc.UseVisualStyleBackColor = False
        '
        'lbl1
        '
        Me.lbl1.Location = New System.Drawing.Point(0, 8)
        Me.lbl1.Name = "lbl1"
        Me.lbl1.Size = New System.Drawing.Size(56, 24)
        Me.lbl1.TabIndex = 10
        Me.lbl1.Text = "1st Band:"
        Me.lbl1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'Label2
        '
        Me.Label2.Location = New System.Drawing.Point(0, 40)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(56, 24)
        Me.Label2.TabIndex = 11
        Me.Label2.Text = "2nd Band:"
        Me.Label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'Label3
        '
        Me.Label3.Location = New System.Drawing.Point(0, 72)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(56, 24)
        Me.Label3.TabIndex = 12
        Me.Label3.Text = "3rd Band:"
        Me.Label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'Label4
        '
        Me.Label4.Location = New System.Drawing.Point(0, 104)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(56, 24)
        Me.Label4.TabIndex = 13
        Me.Label4.Text = "4th Band:"
        Me.Label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        '
        'btnReset
        '
        Me.btnReset.BackColor = System.Drawing.Color.Red
        Me.btnReset.Font = New System.Drawing.Font("Microsoft Sans Serif", 9.0!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnReset.ForeColor = System.Drawing.SystemColors.ControlText
        Me.btnReset.Location = New System.Drawing.Point(120, 216)
        Me.btnReset.Name = "btnReset"
        Me.btnReset.Size = New System.Drawing.Size(56, 40)
        Me.btnReset.TabIndex = 14
        Me.btnReset.Text = "Reset"
        Me.btnReset.UseVisualStyleBackColor = False
        '
        'Form1
        '
        Me.AcceptButton = Me.btnCalc
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(173, 257)
        Me.Controls.Add(Me.btnReset)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.lbl1)
        Me.Controls.Add(Me.Panel2)
        Me.Controls.Add(Me.btnCalc)
        Me.Controls.Add(Me.Panel1)
        Me.Controls.Add(Me.lblAns)
        Me.Controls.Add(Me.Panel3)
        Me.Controls.Add(Me.cmb4)
        Me.Controls.Add(Me.cmb3)
        Me.Controls.Add(Me.cmb2)
        Me.Controls.Add(Me.cmb1)
        Me.Controls.Add(Me.pnlBack)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        Me.ImeMode = System.Windows.Forms.ImeMode.Off
        Me.MaximizeBox = False
        Me.Name = "Form1"
        Me.Text = "Resistor Bands"
        Me.pnlBack.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub
    Friend WithEvents cmb1 As System.Windows.Forms.ComboBox
    Friend WithEvents cmb2 As System.Windows.Forms.ComboBox
    Friend WithEvents cmb3 As System.Windows.Forms.ComboBox
    Friend WithEvents cmb4 As System.Windows.Forms.ComboBox
    Friend WithEvents Panel1 As System.Windows.Forms.Panel
    Friend WithEvents pnlBack As System.Windows.Forms.Panel
    Friend WithEvents Panel2 As System.Windows.Forms.Panel
    Friend WithEvents Panel4 As System.Windows.Forms.Panel
    Friend WithEvents Panel3 As System.Windows.Forms.Panel
    Friend WithEvents lblAns As System.Windows.Forms.Label
    Friend WithEvents btnCalc As System.Windows.Forms.Button
    Friend WithEvents lbl1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents btnReset As System.Windows.Forms.Button

End Class
