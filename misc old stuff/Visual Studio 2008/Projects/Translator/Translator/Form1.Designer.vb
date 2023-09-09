<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Translator
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Translator))
        Me.lblText = New System.Windows.Forms.Label
        Me.lblASCII = New System.Windows.Forms.Label
        Me.txtASCII = New System.Windows.Forms.TextBox
        Me.txtText = New System.Windows.Forms.TextBox
        Me.lblmessage = New System.Windows.Forms.Label
        Me.txtBin = New System.Windows.Forms.TextBox
        Me.lblBin = New System.Windows.Forms.Label
        Me.btnConvert = New System.Windows.Forms.Button
        Me.mnuHelp = New System.Windows.Forms.MenuStrip
        Me.mnuAbout = New System.Windows.Forms.ToolStripMenuItem
        Me.mnuwhat = New System.Windows.Forms.ToolStripMenuItem
        Me.mnuAbASCII = New System.Windows.Forms.ToolStripMenuItem
        Me.AbBinary = New System.Windows.Forms.ToolStripMenuItem
        Me.mnuHelp.SuspendLayout()
        Me.SuspendLayout()
        '
        'lblText
        '
        Me.lblText.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblText.Location = New System.Drawing.Point(0, 24)
        Me.lblText.Name = "lblText"
        Me.lblText.Size = New System.Drawing.Size(136, 16)
        Me.lblText.TabIndex = 2
        Me.lblText.Text = "Text:"
        '
        'lblASCII
        '
        Me.lblASCII.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblASCII.Location = New System.Drawing.Point(136, 24)
        Me.lblASCII.Name = "lblASCII"
        Me.lblASCII.Size = New System.Drawing.Size(136, 16)
        Me.lblASCII.TabIndex = 2
        Me.lblASCII.Text = "ASCII:"
        '
        'txtASCII
        '
        Me.txtASCII.AccessibleRole = System.Windows.Forms.AccessibleRole.None
        Me.txtASCII.CausesValidation = False
        Me.txtASCII.HideSelection = False
        Me.txtASCII.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.txtASCII.Location = New System.Drawing.Point(136, 40)
        Me.txtASCII.MaxLength = 2147483647
        Me.txtASCII.Multiline = True
        Me.txtASCII.Name = "txtASCII"
        Me.txtASCII.Size = New System.Drawing.Size(128, 128)
        Me.txtASCII.TabIndex = 5
        '
        'txtText
        '
        Me.txtText.AcceptsReturn = True
        Me.txtText.AccessibleRole = System.Windows.Forms.AccessibleRole.None
        Me.txtText.CausesValidation = False
        Me.txtText.HideSelection = False
        Me.txtText.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.txtText.Location = New System.Drawing.Point(0, 40)
        Me.txtText.MaxLength = 2147483647
        Me.txtText.Multiline = True
        Me.txtText.Name = "txtText"
        Me.txtText.Size = New System.Drawing.Size(128, 104)
        Me.txtText.TabIndex = 5
        '
        'lblmessage
        '
        Me.lblmessage.ForeColor = System.Drawing.Color.Red
        Me.lblmessage.Location = New System.Drawing.Point(168, 224)
        Me.lblmessage.Name = "lblmessage"
        Me.lblmessage.Size = New System.Drawing.Size(104, 40)
        Me.lblmessage.TabIndex = 7
        Me.lblmessage.Text = "Seperate ASCII and binary numbers with a  space"
        '
        'txtBin
        '
        Me.txtBin.AccessibleRole = System.Windows.Forms.AccessibleRole.None
        Me.txtBin.CausesValidation = False
        Me.txtBin.HideSelection = False
        Me.txtBin.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.txtBin.Location = New System.Drawing.Point(0, 168)
        Me.txtBin.MaxLength = 2147483647
        Me.txtBin.Multiline = True
        Me.txtBin.Name = "txtBin"
        Me.txtBin.Size = New System.Drawing.Size(168, 104)
        Me.txtBin.TabIndex = 8
        '
        'lblBin
        '
        Me.lblBin.Font = New System.Drawing.Font("Microsoft Sans Serif", 10.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblBin.Location = New System.Drawing.Point(0, 144)
        Me.lblBin.Name = "lblBin"
        Me.lblBin.Size = New System.Drawing.Size(128, 24)
        Me.lblBin.TabIndex = 9
        Me.lblBin.Text = "Binary:"
        '
        'btnConvert
        '
        Me.btnConvert.Location = New System.Drawing.Point(168, 176)
        Me.btnConvert.Name = "btnConvert"
        Me.btnConvert.Size = New System.Drawing.Size(96, 40)
        Me.btnConvert.TabIndex = 10
        Me.btnConvert.Text = "Convert!"
        Me.btnConvert.UseVisualStyleBackColor = True
        '
        'mnuHelp
        '
        Me.mnuHelp.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.mnuAbout})
        Me.mnuHelp.Location = New System.Drawing.Point(0, 0)
        Me.mnuHelp.Name = "mnuHelp"
        Me.mnuHelp.Size = New System.Drawing.Size(266, 24)
        Me.mnuHelp.TabIndex = 11
        Me.mnuHelp.Text = "MenuStrip1"
        '
        'mnuAbout
        '
        Me.mnuAbout.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.mnuwhat, Me.mnuAbASCII, Me.AbBinary})
        Me.mnuAbout.Name = "mnuAbout"
        Me.mnuAbout.Size = New System.Drawing.Size(52, 20)
        Me.mnuAbout.Text = "About"
        '
        'mnuwhat
        '
        Me.mnuwhat.Name = "mnuwhat"
        Me.mnuwhat.Size = New System.Drawing.Size(143, 22)
        Me.mnuwhat.Text = "What Is This?"
        '
        'mnuAbASCII
        '
        Me.mnuAbASCII.Name = "mnuAbASCII"
        Me.mnuAbASCII.Size = New System.Drawing.Size(143, 22)
        Me.mnuAbASCII.Text = "About ASCII"
        '
        'AbBinary
        '
        Me.AbBinary.Name = "AbBinary"
        Me.AbBinary.Size = New System.Drawing.Size(143, 22)
        Me.AbBinary.Text = "About Binary"
        '
        'Translator
        '
        Me.AcceptButton = Me.btnConvert
        Me.AllowDrop = True
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(266, 275)
        Me.Controls.Add(Me.btnConvert)
        Me.Controls.Add(Me.lblBin)
        Me.Controls.Add(Me.txtBin)
        Me.Controls.Add(Me.lblmessage)
        Me.Controls.Add(Me.txtText)
        Me.Controls.Add(Me.txtASCII)
        Me.Controls.Add(Me.lblASCII)
        Me.Controls.Add(Me.lblText)
        Me.Controls.Add(Me.mnuHelp)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow
        Me.HelpButton = True
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.MainMenuStrip = Me.mnuHelp
        Me.MaximizeBox = False
        Me.Name = "Translator"
        Me.ShowIcon = False
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Translator"
        Me.TransparencyKey = System.Drawing.Color.FromArgb(CType(CType(255, Byte), Integer), CType(CType(192, Byte), Integer), CType(CType(192, Byte), Integer))
        Me.mnuHelp.ResumeLayout(False)
        Me.mnuHelp.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents lblText As System.Windows.Forms.Label
    Friend WithEvents lblASCII As System.Windows.Forms.Label
    Friend WithEvents lblmessage As System.Windows.Forms.Label
    Friend WithEvents lblBin As System.Windows.Forms.Label
    Friend WithEvents btnConvert As System.Windows.Forms.Button
    Private WithEvents txtASCII As System.Windows.Forms.TextBox
    Private WithEvents txtText As System.Windows.Forms.TextBox
    Private WithEvents txtBin As System.Windows.Forms.TextBox
    Friend WithEvents mnuHelp As System.Windows.Forms.MenuStrip
    Friend WithEvents mnuAbout As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents mnuwhat As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents mnuAbASCII As System.Windows.Forms.ToolStripMenuItem
    Friend WithEvents AbBinary As System.Windows.Forms.ToolStripMenuItem

End Class
