program Test___class_dojogen___;
uses TestUnit, ___class_dojogen___Unit;

procedure Test___class_dojogen___;
begin
  InitTest('___class_dojogen___ de 1 deve retornar -1'); 
  Assert(___class_dojogen___(1) = -1);
end;

begin
  StartTests;
  TestCase('___class_dojogen___', @Test___class_dojogen___);		  
  EndTests;
end.
