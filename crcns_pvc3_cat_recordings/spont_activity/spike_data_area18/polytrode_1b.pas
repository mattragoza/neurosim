unit ElectrodeTypes;
interface
uses Windows;
const
  MAXCHANS = 64;
  MAXELECTRODEPOINTS = 12;
  KNOWNELECTRODES = 32;

type
  TElectrode = record
    NumPoints : integer;
    Outline : array[0..MAXELECTRODEPOINTS-1] of TPoint;  //in microns
    NumSites : Integer;
    SiteLoc : array[0..MAXCHANS-1] of TPoint; //in microns
    TopLeftSite, BotRightSite : TPoint;
    CenterX : Integer;
    SiteSize : TPoint; //in microns
    RoundSite : boolean;
    Created : boolean;
    Name : ShortString;
    Description : ShortString;
  end;

function GetElectrode(var Electrode : TElectrode; Name : ShortString) : boolean;

var  KnownElectrode : array[0..KNOWNELECTRODES -1] of TElectrode ;

implementation

procedure MakeKnownElectrodes;
begin
    {µMAP54_1b: this mapping is correct for the cat data
     all dimensions are specified in microns}
    with KnownElectrode[18] do
    begin
      Name := 'µMap54_1b';
      Description := 'µMap54_1b, 50µm spacing';
      SiteSize.x := 15;
      SiteSize.y := 15;
      RoundSite := TRUE;
      Created := FALSE;

      NumPoints := 8;
      Outline[0].x := -100;
      Outline[0].y := 0;
      Outline[1].x := -100;
      Outline[1].y := 900;
      Outline[2].x := -20;
      Outline[2].y := 1200;
      Outline[3].x := 0;
      Outline[3].y := 1250;
      Outline[4].x := 20;
      Outline[4].y := 1200;
      Outline[5].x := 100;
      Outline[5].y := 900;
      Outline[6].x := 100;
      Outline[6].y := 0;
      Outline[7].x := Outline[0].x;
      Outline[7].y := Outline[0].y;

      NumSites := 54;
      CenterX := 0;
      SiteLoc[0].x := -43;
      SiteLoc[0].y := 900;
      SiteLoc[1].x := -43;
      SiteLoc[1].y := 850;
      SiteLoc[2].x := -43;
      SiteLoc[2].y := 800;
      SiteLoc[3].x := -43;
      SiteLoc[3].y := 750;
      SiteLoc[4].x := -43;
      SiteLoc[4].y := 700;
      SiteLoc[5].x := -43;
      SiteLoc[5].y := 650;
      SiteLoc[6].x := -43;
      SiteLoc[6].y := 600;
      SiteLoc[7].x := -43;
      SiteLoc[7].y := 550;
      SiteLoc[8].x := -43;
      SiteLoc[8].y := 500;
      SiteLoc[9].x := -43;
      SiteLoc[9].y := 450;
      SiteLoc[10].x := -43;
      SiteLoc[10].y := 400;
      SiteLoc[11].x := -43;
      SiteLoc[11].y := 350;
      SiteLoc[12].x := -43;
      SiteLoc[12].y := 300;
      SiteLoc[13].x := -43;
      SiteLoc[13].y := 250;
      SiteLoc[14].x := -43;
      SiteLoc[14].y := 200;
      SiteLoc[15].x := -43;
      SiteLoc[15].y := 150;
      SiteLoc[16].x := -43;
      SiteLoc[16].y := 50;
      SiteLoc[17].x := -43;
      SiteLoc[17].y := 100;
      SiteLoc[18].x := 0;
      SiteLoc[18].y := 900;
      SiteLoc[19].x := 0;
      SiteLoc[19].y := 800;
      SiteLoc[20].x := 0;
      SiteLoc[20].y := 700;
      SiteLoc[21].x := 0;
      SiteLoc[21].y := 600;
      SiteLoc[22].x := 0;
      SiteLoc[22].y := 500;
      SiteLoc[23].x := 0;
      SiteLoc[23].y := 400;
      SiteLoc[24].x := 0;
      SiteLoc[24].y := 200;
      SiteLoc[25].x := 0;
      SiteLoc[25].y := 100;
      SiteLoc[26].x := 0;
      SiteLoc[26].y := 300;
      SiteLoc[27].x := 0;
      SiteLoc[27].y := 50;
      SiteLoc[28].x := 0;
      SiteLoc[28].y := 150;
      SiteLoc[29].x := 0;
      SiteLoc[29].y := 250;
      SiteLoc[30].x := 0;
      SiteLoc[30].y := 350;
      SiteLoc[31].x := 0;
      SiteLoc[31].y := 450;
      SiteLoc[32].x := 0;
      SiteLoc[32].y := 550;
      SiteLoc[33].x := 0;
      SiteLoc[33].y := 650;
      SiteLoc[34].x := 0;
      SiteLoc[34].y := 750;
      SiteLoc[35].x := 0;
      SiteLoc[35].y := 850;
      SiteLoc[36].x := 43;
      SiteLoc[36].y := 200;
      SiteLoc[37].x := 43;
      SiteLoc[37].y := 100;
      SiteLoc[38].x := 43;
      SiteLoc[38].y := 50;
      SiteLoc[39].x := 43;
      SiteLoc[39].y := 150;
      SiteLoc[40].x := 43;
      SiteLoc[40].y := 250;
      SiteLoc[41].x := 43;
      SiteLoc[41].y := 300;
      SiteLoc[42].x := 43;
      SiteLoc[42].y := 350;
      SiteLoc[43].x := 43;
      SiteLoc[43].y := 400;
      SiteLoc[44].x := 43;
      SiteLoc[44].y := 450;
      SiteLoc[45].x := 43;
      SiteLoc[45].y := 500;
      SiteLoc[46].x := 43;
      SiteLoc[46].y := 550;
      SiteLoc[47].x := 43;
      SiteLoc[47].y := 600;
      SiteLoc[48].x := 43;
      SiteLoc[48].y := 650;
      SiteLoc[49].x := 43;
      SiteLoc[49].y := 700;
      SiteLoc[50].x := 43;
      SiteLoc[50].y := 750;
      SiteLoc[51].x := 43;
      SiteLoc[51].y := 850;
      SiteLoc[52].x := 43;
      SiteLoc[52].y := 900;
      SiteLoc[53].x := 43;
      SiteLoc[53].y := 800;
    end;
  end;


function GetElectrode(var Electrode : TElectrode; Name : ShortString) : boolean;
var i : integer;
begin
   GetElectrode := FALSE;
   For i := 0 to KNOWNELECTRODES-1 do
     if Name = KnownElectrode[i].Name then
     begin
       Move(KnownElectrode[i], Electrode, SizeOf(TElectrode));
       GetElectrode := TRUE;
     end;
end;

initialization
  MakeKnownElectrodes;

end.
