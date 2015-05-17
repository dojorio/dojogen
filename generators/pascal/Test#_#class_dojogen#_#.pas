program Test#_#class_dojogen#_#;
uses TestUnit, #_#class_dojogen#_#Unit;

procedure Test#_#class_dojogen#_#;
begin
  InitTest('#_#class_dojogen#_# de 1 deve retornar -1'); 
  Assert(#_#class_dojogen#_#(1) = -1);
end;

begin
  StartTests;
  TestCase('#_#class_dojogen#_#', @Test#_#class_dojogen#_#);		  
  EndTests;
end.
