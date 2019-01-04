# -*- coding:utf-8 -*-
"""
@Author: lamborghini
@Date: 2018-12-10 10:34:20
@Desc: ui界面管理
"""

import weakref

g_UIMgr = None


def GetUIMgr():
    global g_UIMgr
    if not g_UIMgr:
        g_UIMgr = CUIManager()
    return g_UIMgr


class CUIManager:
    def __init__(self):
        self.m_BPUI = {}
        self.m_NodeUI = {}
        self.m_PinBtnUI = {}
        self.m_PinUI = {}
        self.m_LineUI = {}

    def AddBPView(self, bpID, oBPView):
        self.m_BPUI[bpID] = weakref.ref(oBPView)

    def DelBPView(self, bpID):
        if bpID in self.m_BPUI:
            del self.m_BPUI[bpID]

    def GetBPView(self, bpID):
        wObj = self.m_BPUI.get(bpID, None)
        if wObj:
            wObj = wObj()
        return wObj

    def AddNodeUI(self, nodeID, oNodeUI):
        self.m_NodeUI[nodeID] = weakref.ref(oNodeUI)

    def DelNodeUI(self, nodeID):
        if nodeID in self.m_NodeUI:
            del self.m_NodeUI[nodeID]

    def GetNodeUI(self, nodeID):
        wObj = self.m_NodeUI.get(nodeID, None)
        if wObj:
            wObj = wObj()
        return wObj

    def AddPinUI(self, pinID, oPinUI):
        self.m_PinUI[pinID] = weakref.ref(oPinUI)

    def DelPinUI(self, pinID):
        if pinID in self.m_PinUI:
            del self.m_PinUI[pinID]

    def GetPinUI(self, pinID):
        wObj = self.m_PinUI.get(pinID, None)
        if wObj:
            wObj = wObj()
        return wObj

    def AddPinBtnUI(self, pinID, oPinbtnUI):
        self.m_PinBtnUI[pinID] = weakref.ref(oPinbtnUI)

    def DelPinBtnUI(self, pinID):
        if pinID in self.m_PinBtnUI:
            del self.m_PinBtnUI[pinID]

    def AddLineUI(self, lineID, oLineUI):
        self.m_LineUI[lineID] = weakref.ref(oLineUI)

    def DelLineUI(self, lineID):
        if lineID in self.m_LineUI:
            del self.m_LineUI[lineID]

    def GetLineUI(self, lineID):
        wObj = self.m_LineUI.get(lineID, None)
        if wObj:
            wObj = wObj()
        return wObj